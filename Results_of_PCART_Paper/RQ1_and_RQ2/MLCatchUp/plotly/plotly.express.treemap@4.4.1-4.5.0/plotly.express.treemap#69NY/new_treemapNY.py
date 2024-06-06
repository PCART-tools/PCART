import plotly.express as px
df = px.data.tips()
fig = px.treemap(df, None, 'total_bill', None, None, None, None, None, None, color_discrete_sequence=None, color_discrete_map={}, path=None)
