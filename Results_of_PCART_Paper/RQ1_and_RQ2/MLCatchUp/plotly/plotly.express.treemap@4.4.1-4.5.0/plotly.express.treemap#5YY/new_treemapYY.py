import plotly.express as px
df = px.data.tips()
fig = px.treemap(df, names=None, path=None)
