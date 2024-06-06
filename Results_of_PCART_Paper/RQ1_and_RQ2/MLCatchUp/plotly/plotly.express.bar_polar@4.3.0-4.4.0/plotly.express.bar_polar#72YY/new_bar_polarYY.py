import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, 'frequency', 'direction', 'strength', None, None, custom_data=None, animation_frame=None, animation_group=None, category_orders={}, labels={}, range_theta=None)
