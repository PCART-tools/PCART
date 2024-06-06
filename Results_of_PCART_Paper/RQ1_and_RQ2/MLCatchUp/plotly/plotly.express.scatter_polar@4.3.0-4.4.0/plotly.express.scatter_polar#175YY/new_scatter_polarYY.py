import plotly.express as px
df = px.data.wind()
fig = px.scatter_polar(df, 'frequency', 'direction', None, None, None, None, None, None, None, None, None, {}, {}, None, color_discrete_map={}, color_continuous_scale=None, range_color=None, range_theta=None)
