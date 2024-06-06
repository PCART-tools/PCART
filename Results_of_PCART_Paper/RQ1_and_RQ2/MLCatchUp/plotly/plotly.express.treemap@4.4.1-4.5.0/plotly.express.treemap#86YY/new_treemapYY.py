import plotly.express as px
df = px.data.tips()
fig = px.treemap(df, None, 'total_bill', None, None, color=None, color_continuous_scale=None, range_color=None, color_continuous_midpoint=None, color_discrete_sequence=None, color_discrete_map={}, hover_name=None, path=None)
