import plotly.express as px
df = px.data.wind()
fig = px.scatter_polar(df, 'frequency', 'direction', None, None, None, None, None, None, None, None, None, {}, {}, None, {}, None, None, None, None, {}, None, 'clockwise', 90, None, None, False, render_mode='auto', range_theta=None)
