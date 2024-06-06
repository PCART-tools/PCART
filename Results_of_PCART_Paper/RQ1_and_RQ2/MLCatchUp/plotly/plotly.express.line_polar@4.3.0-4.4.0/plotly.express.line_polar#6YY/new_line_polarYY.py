import plotly.express as px
df = px.data.wind()
fig = px.line_polar(data_frame=df, r='frequency', range_theta=None)
