import plotly.express as px
df = px.data.wind()
fig = px.line_polar(df, 'frequency', theta='direction', range_theta=None)
