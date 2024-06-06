import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, 'sepal_width', trendline_options=None, trendline_scope='trace')
