import plotly.express as px
df = px.data.tips()
fig = px.treemap(df, None, 'total_bill', None, None, color=None, color_continuous_scale=None, path=None)
