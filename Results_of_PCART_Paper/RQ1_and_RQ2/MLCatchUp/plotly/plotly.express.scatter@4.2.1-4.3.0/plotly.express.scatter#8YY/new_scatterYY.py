import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, 'sepal_width', y='sepal_length', facet_col_wrap=0)
