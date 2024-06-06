import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, 'sepal_width', 'sepal_length', None, symbol=None, size=None, hover_name=None, facet_col_wrap=0)
