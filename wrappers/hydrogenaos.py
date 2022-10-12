import modules.visualization.calculatewf as calculatewf
import modules.graphs.heatmap as heatmap
import os

PARAMETERS = [
    # ('100', '100', [0.075, 0.15, 0.3], 5, 200j),
    # ('100', '200', [0.3, 0.5, 0.7], 10, 200j),
    # ('100', '300', [0.8, 1.2, 1.5], 20, 200j),
    # ('100', '210', [0.3, 0.5, 0.8], 15, 200j),
    # ('100', '310', [0.3, 0.5, 0.8], 20, 200j),
    # ('100', '320', [0.4, 0.6, 0.8], 20, 200j),
    # ('200', '200', [0.6, 0.9, 1.2], 20, 200j),
    # ('200', '210', [0.4, 0.6, 0.8], 20, 200j),
    # ('200', '310', [0.4, 0.6, 0.8], 20, 200j),
    # ('200', '320', [0.4, 0.6, 0.8], 20, 200j),
    # ('210', '300', [0.9, 1.2, 1.5], 30, 200j),
    # ('210', '310', [0.6, 0.9, 1.2], 30, 200j),
    # ('210', '320', [0.6, 0.9, 1.2], 30, 200j),
    # ('300', '300', [0.9, 1.2, 1.5], 30, 200j),
    # ('300', '310', [0.6, 0.9, 1.2], 30, 200j),
    # ('300', '320', [0.7, 1.1, 1.4], 30, 200j),
    # ('210', '210', [0.5, 0.6, 0.8], 20, 200j),
    # ('310', '310', [0.5, 0.8, 1.1], 30, 200j),
]
nlmToName = {'100': '1s', '200': '2s', '300': '3s', '210': '2p', '310': '3p', '320': '3d'}

# for param in PARAMETERS:
#     nlm1, nlm2, rScales, BNDR, STEP = param
#     grid = calculatewf.Grid(BNDR, STEP)
    # r_and_values = grid.plot_two_h_ao(nlm1, nlm2, rScales)
    # values = [elt[1] for elt in r_and_values]
#     filename = f'hydrogen{os.sep}h{nlm1}-{nlm2}'
#     HM = heatmap.Heatmap()
#     HM.main()
#     HM.plot_mixing(r_and_values, grid.X, grid.Y, filename, f'c1*{nlmToName[nlm1]}+c2*{nlmToName[nlm2]}. c1 > 0. Left column: c2 < 0. Right column: c2 > 0')

grid = calculatewf.Grid(20, 200j)
values = grid.plot_all_ao()
HM = heatmap.Heatmap()
HM.main()
filename = f"hydrogen{os.sep}all_aos"
HM.plot_mixing(values, grid.X, grid.Y, filename, 'Hydrogen atom AOs')