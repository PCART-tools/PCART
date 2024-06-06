import plotly.express as px
df = px.data.iris()
fig = px.scatter(data_frame=df, x='sepal_width', y='sepal_length', color=None, symbol=None, size=None, hover_name=None, hover_data=None, custom_data=None, text=None, facet_row=None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None, facet_col_spacing=None, error_x=None, trendline_options=None, trendline_scope='trace')
