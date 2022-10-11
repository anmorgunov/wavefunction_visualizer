import calculatewf
import heatmap 

grid = calculatewf.Grid('geometries/h2.xyz')
values = grid.fill_mo(1)

HM = heatmap.Heatmap()
HM.main()
HM.plot(values, grid.X, grid.Y)

