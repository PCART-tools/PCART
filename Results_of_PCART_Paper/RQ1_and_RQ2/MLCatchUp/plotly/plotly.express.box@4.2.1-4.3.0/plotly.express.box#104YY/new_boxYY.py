import plotly.express as px
df = px.data.tips()
fig = px.box(df, x='time', y='total_bill', color=None, facet_row=None, facet_col=None, hover_name=None, hover_data=None, custom_data=None, animation_frame=None, animation_group=None, category_orders={}, labels={}, facet_col_wrap=0)
