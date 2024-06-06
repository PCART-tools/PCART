import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(df, x='total_bill', y='tip', z=None, facet_col_wrap=0)
