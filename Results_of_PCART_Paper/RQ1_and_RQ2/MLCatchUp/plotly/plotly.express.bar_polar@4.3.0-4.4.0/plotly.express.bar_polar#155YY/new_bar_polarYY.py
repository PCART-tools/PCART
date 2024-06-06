import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, 'frequency', 'direction', 'strength', None, None, None, None, None, {}, {}, None, {}, None, 'relative', 'clockwise', start_angle=90, range_theta=None)
