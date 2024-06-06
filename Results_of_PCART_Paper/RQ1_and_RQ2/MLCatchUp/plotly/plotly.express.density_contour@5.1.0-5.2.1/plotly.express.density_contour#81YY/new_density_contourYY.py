import plotly.express as px
df = px.data.tips()
fig = px.density_contour(df, 'total_bill', 'tip', None, None, None, None, 0, facet_row_spacing=None, facet_col_spacing=None, hover_name=None, hover_data=None, trendline_options=None, trendline_scope='trace')
