import plotly.express as px
df = px.data.tips()
fig = px.violin(df, None, 'total_bill', None, None, None, None, None, None, None, None, {}, {}, None, {}, 'v', 'group', False, False, None, None, None, False, None, template=None, width=None, height=None, facet_col_wrap=0)
