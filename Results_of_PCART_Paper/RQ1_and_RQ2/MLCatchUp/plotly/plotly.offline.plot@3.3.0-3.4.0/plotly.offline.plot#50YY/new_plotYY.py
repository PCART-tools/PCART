import plotly.graph_objs as go
import plotly.offline as pyo
trace = go.Scatter(x=[1, 2, 3], y=[4, 5, 6], include_mathjax=False)
data = [trace]
pyo.plot(data, True, 'Export to plot.ly', True, output_type='file', include_plotlyjs=True, filename='temp-plot.html', auto_open=True, image=None, include_mathjax=False)
