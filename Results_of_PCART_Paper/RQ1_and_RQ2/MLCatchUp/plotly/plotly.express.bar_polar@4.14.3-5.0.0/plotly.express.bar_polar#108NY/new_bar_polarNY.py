import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, 'frequency', 'direction', 'strength', None, None, None, None, None, None, None, None, color_discrete_sequence=None, color_discrete_map=None, pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)
