import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, 'frequency', 'direction', 'strength', None, None, None, None, None, {}, labels={}, color_discrete_sequence=None, color_discrete_map={}, barnorm=None, barmode='relative', range_theta=None)
