import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(df, x='total_bill', text_auto=False)
