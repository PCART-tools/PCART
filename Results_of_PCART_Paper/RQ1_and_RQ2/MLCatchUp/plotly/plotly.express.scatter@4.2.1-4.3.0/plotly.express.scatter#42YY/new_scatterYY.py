import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, 'sepal_width', 'sepal_length', color=None, symbol=None, size=None, hover_name=None, hover_data=None, facet_col_wrap=0)
