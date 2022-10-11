from modules.graphs.graph import Graph
import plotly.graph_objects as go
import numpy as np


class Volume(Graph):

    def __init__(self):
        pass
    
    def plot(self, values, X, Y, Z, fname):

        # values = np.power(values, 2)
        param = 1*10**(-1)
        # fig = go.Figure(data=[go.Surface(z=values,
        #                          x=x, y=y,
        #                          )],)
        # print(np.min(values), np.max(values))
        # values = values * (-1)
        # print(len(values), len(values.flatten()))
        # print(values)
        # print(values[2][5][0.89], values[2][5][-0.89])
        fig = go.Figure(data=go.Volume(
            x=X.flatten(),
            y=Y.flatten(),
            z=Z.flatten(),
            value=values.flatten(),
            isomin=-param,
            isomax=param,
            opacity=0.2, # needs to be small to see through all surfaces
            surface_count=100, # needs to be a large number for good volume rendering
            opacityscale="max",
            colorscale='balance'
            ))
        
        # self._update_fig(fig)
        fig.write_html(f'{fname}.html',)# include_plotlyjs='cdn')

    def main(self):
        pass 




if __name__ == "__main__":
    VM = Volume()
    VM.main()
    # HM.plot(z, X, Y)