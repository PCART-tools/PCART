import plotly.graph_objs as go
import plotly.offline as pyo
trace = go.Scatter(x=[1, 2, 3], y=[4, 5, 6], animation_opts=None)
data = [trace]
pyo.plot(figure_or_data=data, animation_opts=None)
