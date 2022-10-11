import modules.visualization.calculatewf as calculatewf
import modules.graphs.heatmap as heatmap
import modules.graphs.volume as volume
import modules.graphs.surface as surface

import os 
CUR_DIRECTORY = os.sep.join(os.path.dirname(__file__).split(os.sep)[:-1])



# print("Welcome to wavefunction plotter!")
# geom = input(f"Please type the filename (without .xyz) that contains the geometry of your molecule: ")

grid = calculatewf.Grid(10, 300j)
# geom = 'co'
geom = 'c6h6'
grid.do_rhf(os.path.join(CUR_DIRECTORY, 'geometries', f"{geom}.xyz"))
grid.plot_basis_functions('2D')
SCFobject = grid.get_scf_object()
MolObject = SCFobject.get_molecule_object()
# MOs = range(MolObject.nelec[0]+1)

MOs = {12, 13, 14, 15, 16, 17, 19, 21}
for i in MOs:
    values = grid.fill_mo(i)
    filename = f"{geom}{os.sep}{geom}-mo-{i}"
    HM = heatmap.Heatmap()
    HM.main()
    # HM.plot(values, grid.X, grid.Y, filename+'-heatmap', f'MO #{i} of {geom}')
    SF = surface.Surface()
    SF.main()
    # SF.plot(values, grid.X, grid.Y, filename+'-surface', f'MO #{i} of {geom}')


    