import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, 'sepal_width', facet_col_wrap=0)
