import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, 'year', 'pop', None, None, None, None, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, pattern_shape_map=None, range_color=None, color_continuous_midpoint=None, opacity=None, orientation=None, text_auto=False)
