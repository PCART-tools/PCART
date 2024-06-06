import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, 'year', 'pop', None, None, None, 0, None, None, hover_name=None, hover_data=None, pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)
