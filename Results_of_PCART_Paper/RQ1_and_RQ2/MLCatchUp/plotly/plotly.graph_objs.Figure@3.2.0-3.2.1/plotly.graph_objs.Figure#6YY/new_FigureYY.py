import plotly.graph_objs as go
fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[3, 1, 6])], layout=go.Layout(title='My Plot'), skip_invalid=False)
