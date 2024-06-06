from IPython.display import display, HTML
import plotly.offline as py
import plotly.graph_objs as go
py.init_notebook_mode(connected=True)
trace = go.Scatter(x=[1, 2, 3], y=[4, 5, 6])
data = [trace]
py.iplot(figure_or_data=data, show_link=False, link_text='Export to plot.ly', validate=True, auto_play=True)
