import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, 'frequency', 'direction', 'strength', None, hover_data=None, custom_data=None, animation_frame=None, animation_group=None, category_orders={}, range_theta=None)
