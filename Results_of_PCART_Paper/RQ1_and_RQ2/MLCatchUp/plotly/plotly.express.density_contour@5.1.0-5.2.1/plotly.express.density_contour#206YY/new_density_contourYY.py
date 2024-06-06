import plotly.express as px
df = px.data.tips()
fig = px.density_contour(df, 'total_bill', y='tip', z=None, color=None, facet_row=None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None, facet_col_spacing=None, hover_name=None, hover_data=None, animation_frame=None, animation_group=None, category_orders=None, labels=None, orientation=None, color_discrete_sequence=None, color_discrete_map=None, trendline_options=None, trendline_scope='trace')
