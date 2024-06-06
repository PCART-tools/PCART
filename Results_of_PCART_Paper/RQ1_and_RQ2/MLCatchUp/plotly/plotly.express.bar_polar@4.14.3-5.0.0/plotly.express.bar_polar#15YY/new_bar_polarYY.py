import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(data_frame=df, r='frequency', theta='direction', color='strength', pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)
