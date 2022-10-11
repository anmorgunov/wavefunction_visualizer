import modules.visualization.calculatewf as calculatewf
import modules.graphs.heatmap as heatmap
import modules.graphs.volume as volume
import modules.graphs.surface as surface

# grid = calculatewf.Grid(30, 300j)
# grid.do_rhf('geometries/c6h6.xyz')
# grid.plot_basis_functions('2D')
# i = 6
# values = grid.fill_mo(i)

# filename = 'test'
# HM = heatmap.Heatmap()
# HM.main()
# HM.plot(values, grid.X, grid.Y, filename)
# SF = surface.Surface()
# SF.main()
# SF.plot(values, grid.X, grid.Y, f'mo{i+1}')
# grid = calculatewf.Grid('geometries/c6h6.xyz', 5, 40j)
# values3D = grid.fill_mo_3d(i)
# VM = volume.Volume()
# VM.main()
# VM.plot(values3D, grid.X_3D, grid.Y_3D, grid.Z_3D, 'test3D')