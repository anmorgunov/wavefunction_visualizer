from graph import Graph
import plotly.graph_objects as go
import numpy as np


class Heatmap(Graph):

    def __init__(self):
        pass
    
    def plot(self, values, x, y):
        minval = np.min(values)
        maxval = max(np.max(values), abs(np.min(values)))
        zmin, zmax = -maxval, maxval
        if minval >= 0:
            colorscale = [[0, 'black'], [1, 'cyan']]
            zmin = 0
        else:
            colorscale = [[0, 'yellow'], [0.5, 'black'], [1, 'cyan']]

        fig = go.Figure(data=go.Heatmap(
                    z=values.flatten(),
                    x=x.flatten(), y=y.flatten(),
                    colorscale=colorscale,
                    zmin = zmin, zmax=zmax
                    ))
        
        self._update_fig(fig)
        fig.write_html('test.html')

    def main(self):
        pass 




if __name__ == "__main__":
    HM = Heatmap()
    HM.main()
    # HM.plot(z, X, Y)