import plotly.express as px
df = px.data.tips()
fig = px.density_contour(df, 'total_bill', 'tip', None, None, None, facet_col=None, trendline_options=None, trendline_scope='trace')
