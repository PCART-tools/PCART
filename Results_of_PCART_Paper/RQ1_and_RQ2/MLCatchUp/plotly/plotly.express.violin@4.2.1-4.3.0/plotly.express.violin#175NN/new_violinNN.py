import plotly.express as px
df = px.data.tips()
fig = px.violin(df, None, 'total_bill', None, None, None, None, None, None, None, None, {}, {}, None, {}, orientation='v', violinmode='group', log_x=False, facet_col_wrap=0)
