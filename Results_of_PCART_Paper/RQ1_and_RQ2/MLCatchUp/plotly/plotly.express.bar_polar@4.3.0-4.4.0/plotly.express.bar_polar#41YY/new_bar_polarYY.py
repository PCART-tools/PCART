import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, 'frequency', 'direction', 'strength', hover_name=None, hover_data=None, custom_data=None, animation_frame=None, range_theta=None)
