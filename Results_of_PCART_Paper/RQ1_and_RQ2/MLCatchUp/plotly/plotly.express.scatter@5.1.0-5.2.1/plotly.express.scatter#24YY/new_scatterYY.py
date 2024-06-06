import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, 'sepal_width', y='sepal_length', color=None, symbol=None, size=None, trendline_options=None, trendline_scope='trace')
