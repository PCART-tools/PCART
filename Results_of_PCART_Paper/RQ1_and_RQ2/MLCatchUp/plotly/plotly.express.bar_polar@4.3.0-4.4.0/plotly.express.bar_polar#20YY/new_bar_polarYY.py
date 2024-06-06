import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, r='frequency', theta='direction', color='strength', hover_name=None, range_theta=None)
