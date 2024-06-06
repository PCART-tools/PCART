import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, 'frequency', 'direction', 'strength', None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'relative', 'clockwise', 90, None, range_theta=None, log_r=False, pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)
