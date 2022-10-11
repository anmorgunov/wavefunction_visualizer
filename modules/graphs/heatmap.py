from modules.graphs.graph import Graph
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np


class Heatmap(Graph):

    def __init__(self):
        pass
    
    def create_heatmap_trace(self, values, x, y, minval, maxval):
        zmin, zmax = -maxval, maxval
        if minval >= 0:
            colorscale = [[0, 'black'], [1, 'cyan']]
            zmin = 0
        else:
            colorscale = [[0, 'yellow'], [0.5, 'black'], [1, 'cyan']]

        return go.Heatmap(
                    z=values.flatten(),
                    x=x.flatten(), y=y.flatten(),
                    colorscale=colorscale,
                    # coloraxis="coloraxis",
                    zmin = zmin, zmax=zmax
                    )

    def determine_min_max(self, values):
        minval = np.min(values)
        maxval = max(np.max(values), abs(np.min(values)))
        if maxval < 1e-6: maxval = 1e-2
        return minval, maxval
        
    def plot(self, values, x, y, filename, title):
        fig = go.Figure()
        minval, maxval = self.determine_min_max(values)
        fig.add_trace(self.create_heatmap_trace(values, x, y, minval, maxval))
        self._update_fig(fig, 720, 720, title)
        # fig.write_html(f'{filename}.html')
        self.save(fig, filename)

    def plot_w_subplots(self, data, x, y, filename, title):
        total = len(data)
        nCol = 2
        nRow = total // nCol + total % nCol
        fig = make_subplots(rows=nRow, cols=nCol,
                            horizontal_spacing=0.05,
                            vertical_spacing=0.05)
        minval = min([np.min(values[1]) for values in data])
        maxval = min([np.max(values[1]) for values in data])
        # print([np.max(values[1]) for values in data])

        # print(fig.print_grid)
        for i, (r, values) in enumerate(data):
            irow = i // nCol + 1
            icol = i % nCol + 1
            # print(irow, icol)
            fig.append_trace(self.create_heatmap_trace(values, x, y, minval, maxval/1.5), row = irow, col = icol)

        self._update_fig(fig, width=900, height=350*nRow, title=title)

        # fig.show()
        # fig.write_html(f'{filename}.html')
        self.save(fig, filename)


    def main(self):
        pass 




if __name__ == "__main__":
    HM = Heatmap()
    HM.main()
    # HM.plot(z, X, Y)