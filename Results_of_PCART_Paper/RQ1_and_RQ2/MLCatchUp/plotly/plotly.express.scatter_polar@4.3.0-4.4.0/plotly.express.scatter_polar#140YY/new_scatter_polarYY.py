import plotly.express as px
df = px.data.wind()
fig = px.scatter_polar(df, 'frequency', 'direction', None, None, None, None, None, None, None, None, None, {}, labels={}, color_discrete_sequence=None, color_discrete_map={}, range_theta=None)
