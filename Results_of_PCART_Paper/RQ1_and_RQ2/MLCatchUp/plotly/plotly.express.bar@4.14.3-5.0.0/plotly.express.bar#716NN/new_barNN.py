import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, 'year', 'pop', None, None, None, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, color_discrete_map=None, color_continuous_scale=None, range_color=None, color_continuous_midpoint=None, opacity=None, orientation=None, barmode='relative', log_x=False, log_y=False, range_x=None, range_y=None, title=None, template=None, width=None, pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)
