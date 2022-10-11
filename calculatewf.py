import numpy as np
import constants 
from tools import sphericals
import scfsolver

A0 = constants.A0

class Grid:

    def __init__(self, geom, boundary=10, step=200j):
        BNDR = boundary
        STEP = step
        self.X, self.Y = np.mgrid[-BNDR:BNDR:STEP, -BNDR:BNDR:STEP]
        self.SCF = scfsolver.RHF(geom, 'sto-3g')
        self.SCF.do_rhf()
        # print(self.SCF.GS.analyze())

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

    def find_r(self, x, y):
        return np.sqrt(x**2+y**2)

    def find_theta(self, x, y):
        if x == 0:
            return np.pi/2
        theta = np.arctan(y/x)
        if x < 0: return theta + np.pi
        return theta 

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
                def gto_eval(x, y):
                    val = 0
                    r = self.find_r(x, y)
                    for i, coeftuple in enumerate(coeffs):
                        # if i == 0: continue # skip the angular momentum nuumber
                        exponent, prefactor = coeftuple
                        val += ANGULAR[nl](x, y, 0, exponent) * prefactor * np.exp(-1*exponent * (r**2))
                    # val = val * sphericals.s_orbital()
                    # if val < THRESHOLD: return 0
                    return val
                return lambda x, y: gto_eval(x-x_0, y-y_0)
            return set_origin
        return sto_ng_nl
    
    def fill_mo(self, index):
        # print(self.MO)
        # print(self.atomToOrbs)
        atomWFs = []
        # for atom, coordinates in geometry:
        print(self.MOL.ao_labels())
        for primitive in self.MOL.ao_labels():
            # print(primitive, primitive.split())
            counter, atom, nl = primitive.split()
            atomPosition = self.GEOMETRY[int(counter)][1] #first element is symbol name
            # print(atom, nl, atomPosition)
            # print(atom, nl)
            coeffs = self.atomToOrbs[atom][nl[:2]]
            # print(coeffs)
            orbital = self.sto_ng(nl)(coeffs)
            atomwf = np.vectorize(orbital(atomPosition))(self.X, self.Y)
            atomWFs.append(atomwf)
        
        # print(self.MO)
        # print([c[index] for c in self.MO])
        scaledWFs = [c[index] * wf for c, wf in zip(self.MO, atomWFs)]
        WFvalue = np.add(scaledWFs[0], scaledWFs[1])

        for i, wf in enumerate(scaledWFs):
            if i <= 1: continue
            WFvalue = np.add(WFvalue, wf)
 
        return WFvalue

    def main():
        pass


if __name__ == "__main__":
    grid = Grid('geometries/co.xyz')
    grid.fill_mo(6)