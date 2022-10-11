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
        self.SCF = scfsolver.RHF(geom, 'minao')
        self.SCF.do_rhf()

    def find_r(self, x, y):
        return np.sqrt(x**2+y**2)

    def find_theta(self, x, y):
        if x == 0:
            return np.pi/2
        theta = np.arctan(y/x)
        if x < 0: return theta + np.pi
        return theta 

    def s_gto(self, coeffs):
        def set_origin(origin):
            x_0, y_0, z_0 = origin
            def gto_eval(x, y):
                val = 0
                r = self.find_r(x, y)
                for i, coeftuple in enumerate(coeffs):
                    if i == 0: continue # skip the angular momentum nuumber
                    exponent, prefactor = coeftuple
                    val += prefactor * np.exp(-1*exponent * (r**2))
                val = val * sphericals.s_orbital()
                # if val < THRESHOLD: return 0
                return val
            return lambda x, y: gto_eval(x-x_0, y-y_0)
        return set_origin
    
    def fill_mo(self, index):
        geometry = self.SCF.get_geometry() 
        MO = self.SCF.get_mo_coeff()
        atomWFs = []
        for atom, coordinates in geometry:
            orbital = self.s_gto(self.SCF.get_basis()[atom][0]) #zero indexing because you take only the first orbital
            atomwf = np.vectorize(orbital(coordinates))(self.X, self.Y)
            atomWFs.append(atomwf)
        

        scaledWFs = [c[index] * wf for c, wf in zip(MO, atomWFs)]
        WFvalue = np.add(scaledWFs[0], scaledWFs[1])

        for i, wf in enumerate(scaledWFs):
            if i <= 1: continue
            WFValue = np.add(WFValue, wf)
 
        return WFvalue

    def main():
        pass


if __name__ == "__main__":
    grid = Grid('geometries/h2.xyz')
    grid.fill_mo(1)