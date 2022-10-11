import constants 
import numpy as np 

A0 = constants.A0
class HydrogenWF:

    def __init__(self):
        pass 

    def psi100(self, x, y):
        r = self.find_r(x, y)
        theta = self.find_theta(x, y)
        Z = 1
        rho = Z*r/A0
        val = 1/np.sqrt(np.pi) * (Z/A0)**1.5 * np.exp(-rho)
        return val

    def psi210(self, x, y):
        r = self.find_r(x, y)
        theta = self.find_theta(x, y)
        val = (1/(4*np.sqrt(2*np.pi)*A0**(1.5))) * (r/A0) * (np.exp(-r/(2*A0))) * np.cos(theta)
        # return 1
        return val

    def psi310(self, x, y):
        r = self.find_r(x, y)
        theta = self.find_theta(x, y)
        
        Z = 1
        rho = Z*r/A0
        # radial = 1/(9*np.sqrt(6))*rho*(4-rho)*np.exp(-r/2)
        # angular = np.sqrt(3)*x/r * np.sqrt(1/4*np.pi)
        val = 1/81 * np.sqrt(2/np.pi) * (Z/A0)**(1.5) * (6*r-rho**2)*np.exp(-rho/3)*np.cos(theta)
        # return radial*angular
        return val