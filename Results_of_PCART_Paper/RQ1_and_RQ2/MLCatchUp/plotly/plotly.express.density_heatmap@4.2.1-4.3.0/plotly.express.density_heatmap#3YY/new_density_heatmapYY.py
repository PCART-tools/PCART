import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(data_frame=df, facet_col_wrap=0)
