import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, 'year', 'pop', None, None, None, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, color_continuous_midpoint=None, opacity=None, pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)
