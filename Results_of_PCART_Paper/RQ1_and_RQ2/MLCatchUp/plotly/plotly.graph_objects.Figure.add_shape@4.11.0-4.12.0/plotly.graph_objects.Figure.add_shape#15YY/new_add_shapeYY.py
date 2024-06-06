import plotly.graph_objects as go
fig = go.Figure()
trace1 = go.Bar(x=[1, 2, 3], y=[4, 5, 6], name='Bar Trace')
fig.add_trace(trace1)
fig.add_shape(arg=None, editable=None, fillcolor=None, fillrule=None, exclude_empty_subplots=None)
