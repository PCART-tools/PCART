import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, 'year', 'pop', None, None, None, None, None, None, None, None, None, None, None, None, animation_group=None, category_orders={}, labels={}, color_discrete_sequence=None, color_discrete_map={}, facet_col_wrap=0)
