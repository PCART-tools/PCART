import plotly.express as px
df = px.data.tips()
fig = px.treemap(df, None, values='total_bill', parents=None, ids=None, path=None)
