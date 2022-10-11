import plotly.graph_objects as go

import pandas as pd
import numpy as np

def find_r(x, y):
    return np.sqrt(x**2+y**2)

def find_theta(x, y):
    if x == 0:
        return np.pi/2
    theta = np.arctan(y/x)
    if x < 0: return theta + np.pi
    return theta 

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


A0 = 1#5.29177210903*(10**(-11))

# xs, ys, zs = [], [], []

# BNDR = 60
# div = 5

# for dx in range(-BNDR, BNDR):
#     x = dx/div
#     xs.append(x)
# for dy in range(-BNDR, BNDR):
#     y = dy/div
#     ys.append(y)
#         # zs.append(psi210(x, y)**2)

# print('before')
# # zs = [zs]*len(xs)
# f = open('dataset.csv', 'w')
# print(len(xs), len(ys))
# # f.write(','+','.join([str(index) for index in range(len(xs))])+'\n')
# for i, x in enumerate(xs):
#     # values = f'{i},'
#     values = ''
#     for j, y in enumerate(ys):
#         values += str(psi210(x, y)**1)
#         if j != len(ys) - 1: values += ','
#     if i != len(xs) - 1: values += '\n'
#     f.write(values)
# f.close()
# print('after')
# print(xs, ys, zs)
# threshold = 5
# z_data = pd.read_csv('dataset.csv')
# z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

# print(type(z_data))
# z_data = pd.array(zs*len(xs))
# print(z_data)

# z = z_data.values
# print(z, len(z), type(z))
BNDR = 30
STEP = 200j
X, Y = np.mgrid[-BNDR:BNDR:STEP, -BNDR:BNDR:STEP]
# print(X, len(X))
z = np.vectorize(psi310)(X, Y)
# sh_0, sh_1 = z.shape
# x, y = np.linspace(0, 1, sh_0), np.linspace(0, 1, sh_1)
# print('here')
# print(z, type(z), len(z))
# fig = go.Figure(data=[go.Surface(z=z,
#                                 #  x=X.flatten(), y=Y.flatten(),
#                                  )],)
# # print('fig created')
# fig.update_layout(title='Mt Bruno Elevation', autosize=True,
#                 #   width=500, height=500,
#                   margin=dict(l=65, r=50, b=65, t=90),
#         scene = dict(
#                     # xaxis = dict(nticks=4, range=[min(xs),max(xs)],),
#                     #  yaxis = dict(nticks=4, range=[min(ys),max(ys)],),
#                     #  zaxis = dict(nticks=4, range=[min(zs),max(zs)],),
#                      ),
#                 )
# fig.show()

# fig = go.Figure(data =
#     go.Contour(
#         z=z
#     ))
# fig.show()

# fig = go.Figure(data=go.Heatmap(
#                     z=z,
#                     colorscale=[[0, 'yellow'], [0.5, 'black'], [1, 'cyan']]))
# fig.update_layout(title='Mt Bruno Elevation', autosize=False,
#                   width=800, height=800,
#                   margin=dict(l=65, r=50, b=65, t=90),
#                     )
# fig.write_html('test.html')
# fig.show()

# with open('h2o.cube', 'w') as f:
#     f.write('''Electron density in real space (e/Bohr^3)
# PySCF Version: 2.0.1  Date: Sat Oct  8 14:47:07 2022
#     2   -3.000000   -3.000000   -3.000000
#    80    0.075949    0.000000    0.000000
#    80    0.000000    0.075949    0.000000
#    80    0.000000    0.000000    0.099870
#     1    0.000000    0.000000    0.000000    0.000000
#     1    0.000000    0.000000    0.000000    1.889726\n''')
#     vox = 0.075949
#     N = 80
#     for ix in range(N):
#         for iy in range(N):
#             for iz in range(N):
#                 x, y, z = ix*vox, iy*vox, iz*vox
#                 f.write(str(psi210(x, y)**2)+' ')
#                 if iz % 6 == 5:
#                     f.write('\n')
#             f.write('\n')

    # for (ix=0;ix<NX;ix++) {
    #     for (iy=0;iy<NY;iy++) {
    #         for (iz=0;iz<NZ;iz++) {
    #         printf("%g ",data[ix][iy][iz]);
    #         if (iz % 6 == 5)
    #             printf("\n");
    #         }
    #         printf("\n");
    #     }
    # }

def find_r(x, y, z):
    return np.sqrt(x**2+y**2+z**2)

def find_theta(x, y):
    return np.arctan2(y, x)
    theta = np.arctan(y/x)
    if x < 0: return theta + np.pi
    return theta 

def psi210(x, y, z):
    r = find_r(x, y, z)
    theta = find_theta(x, y)
    val = (1/(4*np.sqrt(2*np.pi)*A0**(1.5))) * (r/A0) * (np.exp(-r/(2*A0))) * np.cos(theta)
    # return 1
    return val

import plotly.graph_objects as go
import numpy as np
BNDR = 60
STEP = BNDR*3
X, Y, Z = np.mgrid[-BNDR:BNDR:40j, -BNDR:BNDR:40j, -BNDR:BNDR:40j]
print(X.flatten(), len(X))
vecpsi = np.vectorize(psi210)
# values = np.sin(X*Y*Z) / (X*Y*Z)
values = vecpsi(X, Y, Z)
param = 1*10**(-6)
import volume 
VM = volume.Volume()
VM.main()
VM.plot(values, X, Y, Z, 'test')
# print(type(values), values)
print(values.flatten(), len(values))
# fig = go.Figure(data=go.Volume(
#     x=X.flatten(),
#     y=Y.flatten(),
#     z=Z.flatten(),
#     value=values.flatten(),
#     isomin=-param,
#     isomax=param,
#     opacity=0.2, # needs to be small to see through all surfaces
#     surface_count=100, # needs to be a large number for good volume rendering
#     opacityscale="extremes",
#     colorscale='RdBu'
#     ))
# fig.show()
# fig.write_html('test.html')