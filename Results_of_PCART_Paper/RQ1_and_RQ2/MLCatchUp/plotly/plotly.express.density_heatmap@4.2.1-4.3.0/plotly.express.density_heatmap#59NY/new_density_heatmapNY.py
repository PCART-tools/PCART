import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(df, 'total_bill', 'tip', None, None, None, None, hover_data=None, animation_frame=None, animation_group=None, facet_col_wrap=0)
