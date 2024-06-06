import plotly.express as px
df = px.data.wind()
fig = px.scatter_polar(data_frame=df, r='frequency', theta='direction', color=None, range_theta=None)
