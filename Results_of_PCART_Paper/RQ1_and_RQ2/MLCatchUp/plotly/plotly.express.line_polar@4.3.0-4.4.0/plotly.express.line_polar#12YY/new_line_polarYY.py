import plotly.express as px
df = px.data.wind()
fig = px.line_polar(df, 'frequency', 'direction', color='strength', range_theta=None)
