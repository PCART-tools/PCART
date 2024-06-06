import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x='sepal_width', y='sepal_length', color=None, symbol=None, size=None, hover_name=None, facet_col_wrap=0)
