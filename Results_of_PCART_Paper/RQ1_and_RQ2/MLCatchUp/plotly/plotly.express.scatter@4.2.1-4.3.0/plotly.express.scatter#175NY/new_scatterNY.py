import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, 'sepal_width', 'sepal_length', None, None, None, None, None, None, None, None, None, None, None, None, error_y_minus=None, animation_frame=None, animation_group=None, facet_col_wrap=0)
