import modules.visualization.calculatewf as calculatewf
import modules.graphs.heatmap
# import heatmap 
# import surface
# import volume 
# print(modules.graphs.heatmap)
grid = calculatewf.Grid('geometries/co.xyz', 5, 200j)
i = 7
# values = grid.fill_mo_3d(i)
values = grid.fill_mo(i)

print(len(grid.X_3D), len(values), len(grid.X_3D.flatten()), len(values.flatten()))
# HM = heatmap.Heatmap()
HM = modules.graphs.heatmap.Heatmap()
HM.main()
HM.plot(values, grid.X, grid.Y)
# SF = surface.Surface()
# SF.main()
# SF.plot(values, grid.X, grid.Y, f'mo{i+1}')
# VM = volume.Volume()
# VM.main()
# VM.plot(values, grid.X_3D, grid.Y_3D, grid.Z_3D, 'test')