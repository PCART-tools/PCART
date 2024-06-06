import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(data_frame=df, range_theta=None)
