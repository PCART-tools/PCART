import plotly.express as px
df = px.data.wind()
fig = px.scatter_polar(df, 'frequency', 'direction', None, None, None, None, None, None, None, None, None, {}, {}, None, {}, None, range_color=None, color_continuous_midpoint=None, symbol_sequence=None, range_theta=None)
