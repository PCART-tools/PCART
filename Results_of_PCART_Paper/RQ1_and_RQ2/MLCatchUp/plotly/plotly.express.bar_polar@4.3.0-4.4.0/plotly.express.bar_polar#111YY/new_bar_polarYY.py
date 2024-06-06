import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, 'frequency', 'direction', 'strength', None, None, None, None, None, category_orders={}, labels={}, color_discrete_sequence=None, color_discrete_map={}, barnorm=None, range_theta=None)
