from pyscf import gto, scf
import constants 

A0 = constants.A0

class RHF:

    def __init__(self, geometry, basis):
        assert basis == 'minao', 'Only minao is currently supported'
        self.GEOM = geometry
        self.BASIS = basis 

    def do_rhf(self):
        mol = gto.M(atom=self.GEOM)
        mol.basis = self.BASIS
        mol.build()
        rhf = scf.RHF(mol)
        rhf.kernel()
        self._geometry = mol._atom
        self.MO_C = rhf.mo_coeff
        self._basis = mol._basis
    
    def get_geometry(self): return self._geometry
    def get_basis(self): return self._basis
    def get_mo_coeff(self): return self.MO_C

    def main():
        pass


if __name__ == "__main__":
    rhf = RHF('geometries/h2.xyz', 'minao')