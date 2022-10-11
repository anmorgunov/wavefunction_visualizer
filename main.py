import calculatewf
import heatmap 
import surface

grid = calculatewf.Grid('geometries/co.xyz', 5)
i = 0
values = grid.fill_mo(i)

# HM = heatmap.Heatmap()
# HM.main()
# HM.plot(values, grid.X, grid.Y)
SF = surface.Surface()
SF.main()
# SF.plot(values, grid.X, grid.Y, f'mo{i+1}')
