import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, 'frequency', 'direction', 'strength', None, None, None, None, None, {}, {}, color_discrete_sequence=None, color_discrete_map={}, barnorm=None, barmode='relative', direction='clockwise', start_angle=90, range_theta=None)
