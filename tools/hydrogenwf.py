import constants 
import numpy as np 

A0 = constants.A0
class HydrogenWF:

    def __init__(self, Z=1, A0=1):
        self.Z = Z
        self.A0 = A0
        self.NLMtofunc = {
            '100': self.psi100,
            '200': self.psi200, 
            '210': self.psi210,
            '300': self.psi300,
            '310': self.psi310,
            '320': self.psi320
        }
    
    def get_nlm_funcs(self):
        return self.NLMtofunc
    
    def find_r(self, x, y, z):
        return np.sqrt(x**2 + y**2 + z**2)
    
    def find_theta(self, x, y):
        return np.arctan2(y, x)

    def psi100(self, x, y, z):
        r = self.find_r(x, y, z)
        rho = self.Z*r/self.A0
        return 1/np.sqrt(np.pi) * (self.Z/self.A0)**1.5 * np.exp(-rho)

    def psi200(self, x, y, z):
        r = self.find_r(x, y, z)
        rho = self.Z*r/self.A0
        return 1/np.sqrt(32*np.pi) * (self.Z/self.A0)**1.5 * np.exp(-rho/2) * (2-rho)

    def psi210(self, x, y, z):
        r = self.find_r(x, y, z)
        theta = self.find_theta(x, y)
        rho = self.Z*r/self.A0
        return 1/np.sqrt(32*np.pi) * (self.Z/self.A0)**1.5 * np.exp(-rho/2) * rho * np.cos(theta)

    def psi300(self, x, y, z):
        r = self.find_r(x, y, z)
        rho = self.Z*r/self.A0
        return 1/(81*np.sqrt(3*np.pi)) * (self.Z/self.A0)**1.5 * np.exp(-rho/3) * (27-18*rho+2*(rho**2))

    def psi310(self, x, y, z):
        r = self.find_r(x, y, z)
        theta = self.find_theta(x, y)
        rho = self.Z*r/(self.A0)
        # return 1/(9*np.sqrt(6)) * rho * (4-rho) * self.Z**(1.5) * np.exp(-rho/2) * np.sqrt(3) * x / r * 1/np.sqrt(4*np.pi)
        return 1/(81*np.sqrt(np.pi/2)) * (self.Z/self.A0)**1.5 * np.exp(-rho/3) * (6*rho - (rho**2)) * np.cos(theta)

    def psi320(self, x, y, z):
        r = self.find_r(x, y, z)
        theta = self.find_theta(x, y)
        rho = self.Z*r/self.A0
        # return 1/(81*np.sqrt(6*np.pi)) * (self.Z/self.A0)**1.5 * np.exp(-rho/3) * (rho**2) * (3*(np.cos(theta)**2) - 1) # Y2,0
        return 1/(81*np.sqrt(6*np.pi/3)) * (self.Z/self.A0)**1.5 * np.exp(-rho/3) * (rho**2) * ((x**2)-(y**2))/(r**2) #x^2-y^2
    
    def main(self):
        pass

if __name__ == "__main__":
    H = HydrogenWF()
    H.main()