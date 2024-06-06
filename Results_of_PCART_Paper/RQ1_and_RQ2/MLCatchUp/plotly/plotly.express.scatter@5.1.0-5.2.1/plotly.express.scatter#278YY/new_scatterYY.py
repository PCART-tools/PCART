import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, 'sepal_width', 'sepal_length', None, None, None, None, None, None, None, None, None, 0, None, None, None, None, None, None, None, animation_group=None, category_orders=None, labels=None, trendline_options=None, trendline_scope='trace')
