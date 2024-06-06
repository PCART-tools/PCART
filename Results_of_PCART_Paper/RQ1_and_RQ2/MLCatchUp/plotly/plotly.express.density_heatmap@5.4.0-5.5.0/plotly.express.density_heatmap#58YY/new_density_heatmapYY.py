import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(df, 'total_bill', 'tip', None, None, None, facet_col_wrap=0, facet_row_spacing=None, facet_col_spacing=None, hover_name=None, text_auto=False)
