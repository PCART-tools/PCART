import plotly.express as px
df = px.data.wind()
fig = px.line_polar(data_frame=df, r='frequency', theta='direction', color='strength', line_dash=None, hover_name=None, hover_data=None, custom_data=None, line_group=None, text=None, animation_frame=None, animation_group=None, category_orders={}, labels={}, color_discrete_sequence=None, color_discrete_map={}, line_dash_sequence=None, line_dash_map={}, direction='clockwise', start_angle=90, range_theta=None)
