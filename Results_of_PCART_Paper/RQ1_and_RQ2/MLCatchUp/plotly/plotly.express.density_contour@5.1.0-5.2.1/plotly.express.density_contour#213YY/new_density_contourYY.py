import plotly.express as px
df = px.data.tips()
fig = px.density_contour(df, 'total_bill', 'tip', None, None, None, None, 0, None, None, None, None, None, None, None, None, orientation=None, color_discrete_sequence=None, color_discrete_map=None, marginal_x=None, trendline_options=None, trendline_scope='trace')
