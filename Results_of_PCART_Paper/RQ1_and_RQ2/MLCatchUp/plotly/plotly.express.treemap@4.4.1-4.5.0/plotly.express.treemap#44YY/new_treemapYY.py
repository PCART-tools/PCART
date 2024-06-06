import plotly.express as px
df = px.data.tips()
fig = px.treemap(df, names=None, values='total_bill', parents=None, ids=None, color=None, color_continuous_scale=None, range_color=None, path=None)
