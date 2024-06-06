import plotly.graph_objs as go
import plotly.offline as pyo
trace = go.Scatter(x=[1, 2, 3], y=[4, 5, 6], animation_opts=None)
data = [trace]
pyo.plot(data, False, 'Export to plot.ly', True, 'file', True, 'temp-plot.html', True, None, image_filename='plot_image', image_width=800, image_height=600, animation_opts=None)
