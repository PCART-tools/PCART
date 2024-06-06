import plotly.express as px
df = px.data.tips()
fig = px.density_contour(df, 'total_bill', 'tip', None, None, None, None, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, False, False, None, range_y=None, histfunc=None, histnorm=None, trendline_options=None, trendline_scope='trace')
