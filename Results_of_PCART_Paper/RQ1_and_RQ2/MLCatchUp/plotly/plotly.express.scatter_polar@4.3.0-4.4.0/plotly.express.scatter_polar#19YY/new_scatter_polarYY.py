import plotly.express as px
df = px.data.wind()
fig = px.scatter_polar(df, 'frequency', theta='direction', color=None, symbol=None, range_theta=None)
