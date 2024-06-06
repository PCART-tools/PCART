import plotly.express as px
df = px.data.wind()
fig = px.line_polar(df, 'frequency', 'direction', 'strength', None, None, hover_data=None, custom_data=None, line_group=None, range_theta=None)
