import plotly.express as px
df = px.data.tips()
fig = px.density_contour(df, 'total_bill', 'tip', None, None, facet_row=None, trendline_options=None, trendline_scope='trace')
