import os 

CUR_DIRECTORY = os.sep.join(os.path.dirname(__file__).split(os.sep)[:-2])

class Graph:

    def __init__(self):
        pass

    def _update_fig(self, fig, width, height, title):
        fig.update_layout(autosize=False,
                        width=width, height=height,
                        margin=dict(l=65, r=50, b=65, t=90),
                        xaxis=dict(
                            showline=True,
                            showgrid=False,
                            showticklabels=True,
                            linecolor='rgb(51, 51, 51)',
                            linewidth=2,
                            ticks='outside',
                            tickfont=dict(
                                family='Helvetica',
                                size=12,
                                color='rgb(51, 51, 51)',
                            ),
                        ),
                        yaxis=dict(
                            showgrid=False,
                            zeroline=False,
                            showline=True,
                            showticklabels=True,
                            linecolor='rgb(51, 51, 51)',
                            linewidth=2,
                            ticks='outside',
                            tickfont=dict(
                                family='Helvetica',
                                size=12,
                                color='rgb(51, 51, 51)',
                            ),
                        ),
                        plot_bgcolor='white',
                        title={
                            'text': title,
                            # 'y':0.9,
                            'x':0.5,
                            'xanchor': 'center',
                            'yanchor': 'top',
                            'font': dict(family='Helvetica',
                                        size=18,
                                        color='#333333'), },)
   
    
    def plot(self):
        pass

    def save(self, fig, filename, doHtml = False):
        if doHtml: fig.write_html(os.path.join(CUR_DIRECTORY, 'output', 'html', f"{filename}.html"), include_plotlyjs='cdn')
        fig.write_image(os.path.join(CUR_DIRECTORY, 'output', 'jpg', f"{filename}.jpg"), scale=4.0)
        fig.write_image(os.path.join(CUR_DIRECTORY, 'output', 'svg', f"{filename}.svg"))

    def main(self):
        pass 


if __name__ == "__main__":
    print(CUR_DIRECTORY)