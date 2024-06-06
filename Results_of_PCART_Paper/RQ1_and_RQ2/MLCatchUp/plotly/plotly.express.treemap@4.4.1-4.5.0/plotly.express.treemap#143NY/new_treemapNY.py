import plotly.express as px
df = px.data.tips()
fig = px.treemap(df, None, 'total_bill', None, None, None, None, None, None, None, color_discrete_map={}, hover_name=None, hover_data=None, custom_data=None, labels={}, title=None, path=None)
