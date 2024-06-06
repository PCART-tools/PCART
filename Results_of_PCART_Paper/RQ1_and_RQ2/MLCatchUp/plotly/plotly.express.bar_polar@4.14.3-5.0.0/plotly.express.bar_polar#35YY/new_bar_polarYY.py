import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, r='frequency', theta='direction', color='strength', hover_name=None, hover_data=None, custom_data=None, pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)
