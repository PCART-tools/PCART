import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(df, facet_col_wrap=0)
