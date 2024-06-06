from IPython.display import display, HTML
import plotly.offline as py
import plotly.graph_objs as go
py.init_notebook_mode(connected=True)
trace = go.Scatter(x=[1, 2, 3], y=[4, 5, 6])
data = [trace]
py.iplot(data, False, 'Export to plot.ly', validate=True, image=None, auto_play=True)
