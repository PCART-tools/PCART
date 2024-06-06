import plotly.express as px
df = px.data.wind()
fig = px.line_polar(df, 'frequency', 'direction', color='strength', line_dash=None, hover_name=None, hover_data=None, custom_data=None, range_theta=None)
