import plotly.express as px
df = px.data.tips()
fig = px.treemap(df, path=None)
