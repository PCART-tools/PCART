import plotly.express as px
df = px.data.tips()
fig = px.violin(df, None, 'total_bill', None, None, None, None, None, None, None, None, {}, {}, None, color_discrete_map={}, orientation='v', violinmode='group', facet_col_wrap=0)
