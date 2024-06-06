import plotly.express as px
df = px.data.tips()
fig = px.density_contour(df, 'total_bill', 'tip', None, None, None, None, 0, None, None, None, None, None, None, None, None, None, color_discrete_sequence=None, color_discrete_map=None, marginal_x=None, marginal_y=None, trendline_options=None, trendline_scope='trace')
