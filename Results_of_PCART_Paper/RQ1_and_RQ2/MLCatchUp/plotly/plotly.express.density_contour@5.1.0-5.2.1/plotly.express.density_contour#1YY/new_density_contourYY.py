import plotly.express as px
df = px.data.tips()
fig = px.density_contour(trendline_options=None, trendline_scope='trace')
