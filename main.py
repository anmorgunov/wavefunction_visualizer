import modules.visualization.calculatewf as calculatewf
import modules.graphs.heatmap as heatmap
import modules.graphs.volume as volume
import modules.graphs.surface as surface
# import heatmap 
# import surface
# import volume 
# print(modules.graphs.heatmap)
grid = calculatewf.Grid(5, 200j)
grid.do_rhf('geometries/c6h6.xyz')
grid.plot_basis_functions('2D')
i = 6
values = grid.fill_mo(i)

# # print(len(grid.X_3D), len(values), len(grid.X_3D.flatten()), len(values.flatten()))
# # HM = heatmap.Heatmap()
# n, l, m = 3, 1, 0
# for n, l, m in ((1, 0, 0), (2, 0, 0), (3, 0, 0), (2, 1, 0), (3, 1, 0), (3, 2, 0)):
# values = grid.plot_hydrogen(n, l, m)
# filename = f'h{n}{l}{m}'
filename = 'test'
HM = heatmap.Heatmap()
HM.main()
HM.plot(values, grid.X, grid.Y, filename)
# SF = surface.Surface()
# SF.main()
# SF.plot(values, grid.X, grid.Y, f'mo{i+1}')
# grid = calculatewf.Grid('geometries/c6h6.xyz', 5, 40j)
# values3D = grid.fill_mo_3d(i)
# VM = volume.Volume()
# VM.main()
# VM.plot(values3D, grid.X_3D, grid.Y_3D, grid.Z_3D, 'test3D')