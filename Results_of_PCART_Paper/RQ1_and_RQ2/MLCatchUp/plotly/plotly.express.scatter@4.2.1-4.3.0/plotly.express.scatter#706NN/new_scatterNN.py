import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, 'sepal_width', 'sepal_length', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, {}, {}, None, {}, None, None, None, None, {}, None, None, None, None, None, None, False, False, range_x=None, range_y=None, facet_col_wrap=0)
