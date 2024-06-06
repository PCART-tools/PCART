import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(df, 'total_bill', 'tip', None, None, None, 0, None, None, None, None, animation_frame=None, animation_group=None, category_orders=None, labels=None, text_auto=False)
