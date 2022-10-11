from modules.graphs.graph import Graph
import plotly.graph_objects as go
import numpy as np


class Surface(Graph):

    def __init__(self):
        pass
    
    def plot(self, values, x, y, fname, title):
        # minval = np.min(values)
        # maxval = max(np.max(values), abs(np.min(values)))
        # zmin, zmax = -maxval, maxval
        # if minval >= 0:
        #     colorscale = [[0, 'black'], [1, 'cyan']]
        #     zmin = 0
        # else:
        #     colorscale = [[0, 'yellow'], [0.5, 'black'], [1, 'cyan']]
        values = np.power(values, 2)
        fig = go.Figure(data=[go.Surface(z=values,
                                 x=x, y=y,
                                 )],)
        # fig = go.Figure(data=go.Heatmap(
        #             z=values.flatten(),
        #             x=x.flatten(), y=y.flatten(),
        #             colorscale=colorscale,
        #             zmin = zmin, zmax=zmax
        #             ))
        
        self._update_fig(fig, 720, 720, title)
        # fig.write_html(f'{fname}.html', include_plotlyjs='cdn')
        self.save(fig, fname, doHtml=True)
        fig.update_layout(scene_camera = dict(
                        eye=dict(x=0, y=0, z=np.max(values)+1)
                    ))
        self.save(fig, fname+'-above', doHtml=True)

    def main(self):
        pass 




if __name__ == "__main__":
    SF = Surface()
    SF.main()
    # HM.plot(z, X, Y)