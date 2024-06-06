import plotly.express as px
df = px.data.wind()
fig = px.line_polar(data_frame=df, range_theta=None)
