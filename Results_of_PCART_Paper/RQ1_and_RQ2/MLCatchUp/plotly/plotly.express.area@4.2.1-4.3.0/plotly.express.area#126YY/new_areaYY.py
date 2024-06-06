import plotly.express as px
df = px.data.gapminder()
fig = px.area(df, 'year', 'pop', 'country', 'continent', None, None, None, None, None, facet_col=None, animation_frame=None, animation_group=None, category_orders={}, labels={}, facet_col_wrap=0)
