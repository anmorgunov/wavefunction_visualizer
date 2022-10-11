from graph import Graph
import plotly.graph_objects as go
import numpy as np
from pyscf import gto, scf

# A0 = 0.529177
A0 = 1

def find_r(x, y):
    return np.sqrt(x**2+y**2)

def find_theta(x, y):
    if x == 0:
        return np.pi/2
    theta = np.arctan(y/x)
    if x < 0: return theta + np.pi
    return theta 

def psi100(x, y):
    r = find_r(x, y)
    theta = find_theta(x, y)
    Z = 1
    rho = Z*r/A0
    val = 1/np.sqrt(np.pi) * (Z/A0)**1.5 * np.exp(-rho)
    return val

def psi210(x, y):
    r = find_r(x, y)
    theta = find_theta(x, y)
    val = (1/(4*np.sqrt(2*np.pi)*A0**(1.5))) * (r/A0) * (np.exp(-r/(2*A0))) * np.cos(theta)
    # return 1
    return val

def psi310(x, y):
    r = find_r(x, y)
    theta = find_theta(x, y)
    
    Z = 1
    rho = Z*r/A0
    # radial = 1/(9*np.sqrt(6))*rho*(4-rho)*np.exp(-r/2)
    # angular = np.sqrt(3)*x/r * np.sqrt(1/4*np.pi)
    val = 1/81 * np.sqrt(2/np.pi) * (Z/A0)**(1.5) * (6*r-rho**2)*np.exp(-rho/3)*np.cos(theta)
    # return radial*angular
    return val

class Heatmap(Graph):

    def __init__(self):
        pass
    
    def plot(self, values, x, y):
        minval = np.min(values)
        maxval = max(np.max(values), abs(np.min(values)))
        zmin, zmax = -maxval, maxval
        if minval >= 0:
            colorscale = [[0, 'black'], [1, 'cyan']]
            zmin = 0
        else:
            colorscale = [[0, 'yellow'], [0.5, 'black'], [1, 'cyan']]

        fig = go.Figure(data=go.Heatmap(
                    z=values.flatten(),
                    x=x.flatten(), y=y.flatten(),
                    colorscale=colorscale,
                    zmin = zmin, zmax=zmax
                    ))
        
        self._update_fig(fig)
        fig.write_html('test.html')

    def main(self):
        pass 


mol = gto.M(atom='h2.xyz')
mol.basis = 'minao'
mol.build()
rhf = scf.RHF(mol)
rhf.kernel()
geometry = mol._atom
C = rhf.mo_coeff
print(geometry, rhf.mo_coeff)
one, two = geometry 

H  = [[0,
        [33.87 , 6.0680e-03],
        [5.095 , 4.5308e-02],
        [1.159 , 0.202822],
        [0.3258, 0.503903],
        [0.1027, 0.383421],]]

_basis = mol._basis
print(mol.ao_labels())

SPHERICAL = {
    'S': 1/(2*np.sqrt(np.pi))
}

THRESHOLD = 10**(-9)
def s_gto(coeffs):
    print(coeffs)
    def set_origin(origin):
        x_0, y_0, z_0 = origin[1]
        def gto_eval(x, y):
            val = 0
            r = find_r(x, y)
            for i, coeftuple in enumerate(coeffs):
                if i == 0: continue # skip the angular momentum nuumber
                exponent, prefactor = coeftuple
                # print(prefactor, exponent)
                val += prefactor * np.exp(-1*exponent * (r**2))
            val = val* SPHERICAL['S']
            # if val < THRESHOLD: return 0
            return val
        return lambda x, y: gto_eval(x-x_0, y-y_0)
    return set_origin

H_1s = s_gto(_basis['H'][0])
# H_1s = s_gto(H[0])

def atompsi210(atom):
    x_0, y_0, z_0 = atom[1]
    return lambda x, y: psi210(x-x_0, y-y_0)

def atompsi100(atom):
    x_0, y_0, z_0 = atom[1]
    return lambda x, y: psi100(x-x_0, y-y_0)

BNDR = 10
STEP = 200j
X, Y = np.mgrid[-BNDR:BNDR:STEP, -BNDR:BNDR:STEP]
# print(X, len(X))
orbital = H_1s
z1 = np.vectorize(orbital(one))(X, Y)
z2 = np.vectorize(orbital(two))(X, Y)
c1 = 0.5341252
c2 = 0.5341252
c1 = -1.42163761
c2 = 1.42163761
z = np.add(c1*z1, c2*z2)
# z = z1

if __name__ == "__main__":
    HM = Heatmap()
    HM.main()
    HM.plot(z, X, Y)