import plotly.express as px
df = px.data.tips()
fig = px.density_contour(df, facet_col_wrap=0)
