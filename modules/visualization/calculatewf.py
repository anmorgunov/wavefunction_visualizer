import numpy as np
import constants 
from tools import sphericals
import modules.scfcalculation.scfsolver as scfsolver
import tools.hydrogenwf as hydrogenwf

A0 = constants.A0

class Grid:

    def __init__(self, boundary=10, step=200j):
        BNDR = boundary
        STEP = step
        self.X, self.Y = np.mgrid[-BNDR:BNDR:STEP, -BNDR:BNDR:STEP]
        self.X_3D, self.Y_3D, self.Z_3D = np.mgrid[-BNDR:BNDR:STEP, -BNDR:BNDR:STEP, -BNDR:BNDR:STEP]

    def do_rhf(self, geom):
        self.SCF = scfsolver.RHF(geom, 'sto-3g')
        self.SCF.do_rhf()
        mol = self.SCF.get_molecule_object()
        C0 = self.SCF.get_mo_coeff()
        # print(self.SCF.GS.analyze())
        labels = mol.ao_labels()
        # print(mol.ao_labels())
        # # print(self.C0)
        
        # orbToContrib = {}
        # for orb in range(mol.nelec[0]):
        #     coeffs = C0[:, orb]
        #     maxCoeff = np.sum(np.power(coeffs, 2))
        #     weights = [round((coeff**2)/maxCoeff*100, 2) for coeff in coeffs]
        #     for i, weight in enumerate(weights):
        #         if weight <= 1: continue
        #         orbToContrib.setdefault(orb, dict())[labels[i]] = weight
        # print(orbToContrib)

        self.GEOMETRY = self.SCF.get_geometry() 
        self.MO = self.SCF.get_mo_coeff()
        self.MOL = self.SCF.get_molecule_object()
        basis = self.SCF.get_basis()
        atomToCoeffs = {}
        lToName = {0: 's', 1: 'p'}

        for atom, coeffArray in basis.items():
            cntrs = {0: 1, 1: 2}
            for elt in coeffArray:
                l, coeffs = elt[0], elt[1:]
                name = f"{cntrs[l]}{lToName[l]}"
                cntrs[l] += 1
                atomToCoeffs.setdefault(atom, dict())[name] = coeffs
        self.atomToOrbs = atomToCoeffs

    def find_r(self, x, y, z):
        return np.sqrt((x**2) + (y**2) + (z**2))

    def sto_ng(self, nl): # n - quantum number, l - angular momentum
        ANGULAR = {
            '1s': sphericals.spherical_s,
            '2s': sphericals.spherical_s,
            '2px': sphericals.spherical_2px,
            '2py': sphericals.spherical_2py,
            '2pz': sphericals.spherical_2pz,
        }
        def sto_ng_nl(coeffs):
            def set_origin(origin):
                x_0, y_0, z_0 = origin
                def gto_eval(x, y, z):
                    val = 0
                    r = self.find_r(x, y, z)
                    for i, coeftuple in enumerate(coeffs):
                        # if i == 0: continue # skip the angular momentum nuumber
                        exponent, prefactor = coeftuple
                        val += ANGULAR[nl](x, y, z, exponent) * prefactor * np.exp(-1*exponent * (r**2))
                    # val = val * sphericals.s_orbital()
                    # if val < THRESHOLD: return 0
                    return val
                return lambda x, y, z: gto_eval(x-x_0, y-y_0, z-z_0)
            return set_origin
        return sto_ng_nl

    def plot_basis_functions(self, dimensionality):
        dToParams = {
            '2D': (self.X, self.Y, 0),
            '3D': (self.X_3D, self.Y_3D, self.Z_3D)
        }
        assert dimensionality in dToParams, f"Dimensionality must be either of {str(dToParams)}"
        # print(self.MO)
        # print(self.atomToOrbs)
        atomWFs = []
        # print(self.MOL.ao_labels())
        for primitive in self.MOL.ao_labels():
            counter, atom, nl = primitive.split()
            atomPosition = self.GEOMETRY[int(counter)][1] #first element is symbol name
            coeffs = self.atomToOrbs[atom][nl[:2]]
            # print(coeffs)
            orbital = self.sto_ng(nl)(coeffs)
            atomwf = np.vectorize(orbital(atomPosition))(*dToParams[dimensionality])
            atomWFs.append(atomwf)

        self.atomWFs = atomWFs

    def fill_mo(self, index):
        # print([c[index] for c in self.MO])
        scaledWFs = [c[index] * wf for c, wf in zip(self.MO, self.atomWFs)]
        WFvalue = np.add(scaledWFs[0], scaledWFs[1])

        for i, wf in enumerate(scaledWFs):
            if i <= 1: continue
            WFvalue = np.add(WFvalue, wf)

        cntr = [0, 0]
        for val in WFvalue.flatten():
            if val < 0: cntr[0] += 1
            else: cntr[1] += 1
        # print(cntr)
        return WFvalue

    def plot_hydrogen(self, n, l, m):
        nlm = f"{n}{l}{m}"
        HydrogenObj = hydrogenwf.HydrogenWF()
        orbital = HydrogenObj.get_nlm_funcs()[nlm]
        return np.vectorize(orbital)(self.X, self.Y, 0)

    def main():
        pass


if __name__ == "__main__":
    grid = Grid('geometries/h2.xyz', 5, 40j)
    # grid.fill_mo(6)
    o = grid.fill_mo_3d(0)
    # print(o)