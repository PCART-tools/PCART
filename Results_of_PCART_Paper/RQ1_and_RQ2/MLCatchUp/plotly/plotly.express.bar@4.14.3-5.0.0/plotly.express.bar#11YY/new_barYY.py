import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, 'year', y='pop', color=None, pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)
