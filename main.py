import calculatewf
import heatmap 

grid = calculatewf.Grid('geometries/co.xyz', 5)
values = grid.fill_mo(7)

HM = heatmap.Heatmap()
HM.main()
HM.plot(values, grid.X, grid.Y)

