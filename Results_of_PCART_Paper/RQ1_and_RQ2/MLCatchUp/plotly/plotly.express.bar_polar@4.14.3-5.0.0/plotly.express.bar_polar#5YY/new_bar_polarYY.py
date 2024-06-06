import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, r='frequency', pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)
