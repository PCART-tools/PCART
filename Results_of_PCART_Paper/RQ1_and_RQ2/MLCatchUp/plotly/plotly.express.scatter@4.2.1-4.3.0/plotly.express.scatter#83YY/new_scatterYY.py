import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, 'sepal_width', 'sepal_length', None, None, None, None, None, custom_data=None, text=None, facet_row=None, facet_col=None, facet_col_wrap=0)
