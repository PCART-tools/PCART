import plotly.express as px
df = px.data.tips()
fig = px.treemap(data_frame=df, names=None, path=None)
