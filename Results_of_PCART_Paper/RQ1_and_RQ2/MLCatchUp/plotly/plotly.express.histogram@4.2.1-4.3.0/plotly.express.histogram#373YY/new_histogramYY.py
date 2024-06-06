import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, None, None, facet_col=None, hover_name=None, hover_data=None, animation_frame=None, animation_group=None, category_orders={}, labels={}, color_discrete_sequence=None, color_discrete_map={}, marginal=None, opacity=None, orientation='v', barmode='relative', barnorm=None, histnorm=None, log_x=False, log_y=False, range_x=None, range_y=None, histfunc=None, cumulative=None, facet_col_wrap=0)
