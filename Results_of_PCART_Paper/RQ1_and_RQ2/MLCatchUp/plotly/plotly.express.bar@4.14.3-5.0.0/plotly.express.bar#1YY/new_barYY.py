import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)
