import plotly.express as px
df = px.data.tips()
fig = px.treemap(df, None, 'total_bill', parents=None, ids=None, color=None, color_continuous_scale=None, range_color=None, color_continuous_midpoint=None, color_discrete_sequence=None, color_discrete_map={}, hover_name=None, hover_data=None, custom_data=None, labels={}, title=None, template=None, width=None, height=None, branchvalues=None, maxdepth=None, path=None)
