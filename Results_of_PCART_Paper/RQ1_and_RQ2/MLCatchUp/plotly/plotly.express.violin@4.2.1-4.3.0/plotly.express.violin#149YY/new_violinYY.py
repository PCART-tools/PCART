import plotly.express as px
df = px.data.tips()
fig = px.violin(df, None, 'total_bill', None, facet_row=None, facet_col=None, hover_name=None, hover_data=None, custom_data=None, animation_frame=None, animation_group=None, category_orders={}, labels={}, color_discrete_sequence=None, color_discrete_map={}, orientation='v', facet_col_wrap=0)
