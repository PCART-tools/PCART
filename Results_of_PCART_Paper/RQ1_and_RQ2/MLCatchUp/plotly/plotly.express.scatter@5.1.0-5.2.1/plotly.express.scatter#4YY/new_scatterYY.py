import plotly.express as px
df = px.data.iris()
fig = px.scatter(data_frame=df, x='sepal_width', trendline_options=None, trendline_scope='trace')
