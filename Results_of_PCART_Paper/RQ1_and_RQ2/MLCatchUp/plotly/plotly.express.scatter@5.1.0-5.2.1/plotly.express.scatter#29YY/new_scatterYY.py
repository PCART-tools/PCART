import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, 'sepal_width', 'sepal_length', None, None, size=None, hover_name=None, trendline_options=None, trendline_scope='trace')
