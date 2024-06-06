import plotly.express as px
df = px.data.tips()
fig = px.box(df, 'time', 'total_bill', None, None, None, None, None, None, None, None, {}, {}, color_discrete_sequence=None, color_discrete_map={}, facet_col_wrap=0)
