import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, None, None, None, None, hover_data=None, animation_frame=None, animation_group=None, category_orders={}, facet_col_wrap=0)
