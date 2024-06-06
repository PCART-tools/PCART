import plotly.express as px
df = px.data.tips()
fig = px.density_contour(df, 'total_bill', 'tip', None, None, None, None, None, None, None, None, category_orders={}, labels={}, color_discrete_sequence=None, color_discrete_map={}, marginal_x=None, marginal_y=None, facet_col_wrap=0)
