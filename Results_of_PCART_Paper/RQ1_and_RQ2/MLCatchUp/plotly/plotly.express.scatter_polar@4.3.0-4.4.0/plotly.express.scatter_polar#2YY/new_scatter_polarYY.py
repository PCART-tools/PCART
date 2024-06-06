import plotly.express as px
df = px.data.wind()
fig = px.scatter_polar(df, range_theta=None)
