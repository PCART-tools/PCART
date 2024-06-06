import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(df, x='total_bill', y='tip', text_auto=False)
