import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, 'sepal_width', 'sepal_length', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, {}, {}, None, {}, None, None, None, None, symbol_map={}, opacity=None, size_max=None, marginal_x=None, marginal_y=None, facet_col_wrap=0)
