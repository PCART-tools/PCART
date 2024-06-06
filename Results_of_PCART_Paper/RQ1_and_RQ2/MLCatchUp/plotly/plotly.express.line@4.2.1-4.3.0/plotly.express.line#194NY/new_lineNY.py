import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, 'year', 'lifeExp', None, None, None, None, None, None, None, None, None, None, None, None, None, animation_frame=None, animation_group=None, category_orders={}, facet_col_wrap=0)
