import plotly.express as px
df = px.data.tips()
fig = px.density_contour(df, 'total_bill', y='tip', z=None, color=None, facet_row=None, facet_col=None, facet_col_wrap=0, trendline_options=None, trendline_scope='trace')
