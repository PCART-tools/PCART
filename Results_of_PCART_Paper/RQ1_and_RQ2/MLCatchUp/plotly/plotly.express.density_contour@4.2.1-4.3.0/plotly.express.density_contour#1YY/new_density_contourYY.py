import plotly.express as px
df = px.data.tips()
fig = px.density_contour(facet_col_wrap=0)
