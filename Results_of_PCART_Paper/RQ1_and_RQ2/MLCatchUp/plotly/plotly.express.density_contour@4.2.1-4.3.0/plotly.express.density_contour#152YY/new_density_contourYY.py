import plotly.express as px
df = px.data.tips()
fig = px.density_contour(df, x='total_bill', y='tip', z=None, color=None, facet_row=None, facet_col=None, hover_name=None, hover_data=None, animation_frame=None, animation_group=None, category_orders={}, labels={}, color_discrete_sequence=None, color_discrete_map={}, marginal_x=None, facet_col_wrap=0)
