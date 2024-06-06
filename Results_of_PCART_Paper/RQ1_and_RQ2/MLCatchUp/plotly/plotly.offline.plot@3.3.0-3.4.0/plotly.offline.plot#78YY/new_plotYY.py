import plotly.graph_objs as go
import plotly.offline as pyo
trace = go.Scatter(x=[1, 2, 3], y=[4, 5, 6], include_mathjax=False)
data = [trace]
pyo.plot(data, True, 'Export to plot.ly', True, 'file', True, 'temp-plot.html', True, None, 'plot_image', 800, 600, include_mathjax=False)
