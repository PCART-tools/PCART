import plotly.express as px
df = px.data.wind()
fig = px.scatter_polar(df, r='frequency', theta='direction', color=None, symbol=None, size=None, hover_name=None, hover_data=None, custom_data=None, range_theta=None)
