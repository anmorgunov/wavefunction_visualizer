import numpy as np 

def spherical_s(x, y, z, exponent):
    return (2 * exponent/np.pi)**(0.75)

def spherical_2px(x, y, z, exponent):
    return ( ( (128 * (exponent**5) / (np.pi**3) )**0.25 ) / ((np.pi**3)**0.25)) * x 

def spherical_2py(x, y, z, exponent):
    return ( ( (128 * (exponent**5) / (np.pi**3) )**0.25 ) / ((np.pi**3)**0.25)) * y 

def spherical_2pz(x, y, z, exponent):
    return ( ( (128 * (exponent**5) / (np.pi**3) )**0.25 ) / ((np.pi**3)**0.25)) * z 

