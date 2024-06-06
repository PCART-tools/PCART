import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, 'frequency', 'direction', 'strength', None, None, None, None, None, {}, {}, None, {}, None, 'relative', direction='clockwise', start_angle=90, range_r=None, log_r=False, title=None, template=None, range_theta=None)
