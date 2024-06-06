import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(text_auto=False)
