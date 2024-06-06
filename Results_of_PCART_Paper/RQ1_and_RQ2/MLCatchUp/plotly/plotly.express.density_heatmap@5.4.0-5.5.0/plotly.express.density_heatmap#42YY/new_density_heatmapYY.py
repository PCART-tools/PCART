import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(df, x='total_bill', y='tip', z=None, facet_row=None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None, text_auto=False)
