import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, 'year', 'pop', None, None, None, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'relative', False, log_y=False, range_x=None, range_y=None, pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)
