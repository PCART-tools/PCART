import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(df, 'total_bill', y='tip', z=None, facet_row=None, text_auto=False)
