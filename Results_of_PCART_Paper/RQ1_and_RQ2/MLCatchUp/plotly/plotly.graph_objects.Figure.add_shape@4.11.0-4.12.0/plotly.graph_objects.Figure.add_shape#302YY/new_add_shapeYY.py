import plotly.graph_objects as go
fig = go.Figure()
trace1 = go.Bar(x=[1, 2, 3], y=[4, 5, 6], name='Bar Trace')
fig.add_trace(trace1)
fig.add_shape(None, None, None, None, None, dict(color='FireBrick', width=3), None, None, None, None, 'line', None, 0, 5, None, None, None, 0, 17, None, None, None, None, col=None, exclude_empty_subplots=None)
