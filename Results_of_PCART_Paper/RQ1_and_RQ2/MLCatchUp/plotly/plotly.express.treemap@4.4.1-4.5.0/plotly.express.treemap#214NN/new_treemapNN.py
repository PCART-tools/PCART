import plotly.express as px
df = px.data.tips()
fig = px.treemap(df, None, 'total_bill', None, None, None, None, None, None, None, {}, None, None, None, {}, None, None, width=None, height=None, branchvalues=None, path=None)
