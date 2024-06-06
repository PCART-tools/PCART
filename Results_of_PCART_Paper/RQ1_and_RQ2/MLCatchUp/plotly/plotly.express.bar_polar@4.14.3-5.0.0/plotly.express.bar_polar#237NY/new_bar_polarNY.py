import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, 'frequency', 'direction', 'strength', None, None, None, None, None, None, None, None, None, None, None, None, color_continuous_midpoint=None, barnorm=None, barmode='relative', direction='clockwise', start_angle=90, pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)
