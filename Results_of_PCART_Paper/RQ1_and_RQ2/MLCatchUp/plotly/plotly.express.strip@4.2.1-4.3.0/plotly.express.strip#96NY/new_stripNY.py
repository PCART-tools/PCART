import plotly.express as px
df = px.data.tips()
fig = px.strip(df, 'total_bill', 'day', None, None, None, None, None, None, animation_frame=None, animation_group=None, category_orders={}, labels={}, facet_col_wrap=0)
