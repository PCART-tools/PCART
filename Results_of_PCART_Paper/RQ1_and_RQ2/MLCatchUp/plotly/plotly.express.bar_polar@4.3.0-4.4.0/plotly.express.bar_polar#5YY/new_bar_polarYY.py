import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, r='frequency', range_theta=None)
