import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, 'frequency', theta='direction', color='strength', hover_name=None, hover_data=None, custom_data=None, animation_frame=None, animation_group=None, category_orders={}, labels={}, color_discrete_sequence=None, range_theta=None)
