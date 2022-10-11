import numpy as np 

def s_orbital(*args):
    return 1/(2*np.sqrt(np.pi))

def p_orbital(r, theta, phi, coord):
    return 1/2 * np.sqrt(3/np.pi) * coord/r

def px_orbital(r, theta, phi, x):
    return p_orbital(r, theta, phi, x)

