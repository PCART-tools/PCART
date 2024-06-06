import plotly.express as px
df = px.data.tips()
fig = px.box(df, 'time', 'total_bill', None, None, None, None, None, None, None, None, {}, {}, None, {}, 'v', 'group', False, False, None, None, None, False, None, None, width=None, height=None, facet_col_wrap=0)
