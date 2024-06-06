import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, 'sepal_width', 'sepal_length', None, None, None, None, None, None, None, None, None, 0, None, facet_col_spacing=None, error_x=None, error_x_minus=None, trendline_options=None, trendline_scope='trace')
