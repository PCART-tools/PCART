import plotly.express as px
df = px.data.tips()
fig = px.violin(df, None, 'total_bill', None, None, None, None, None, None, None, None, {}, {}, None, {}, 'v', 'group', False, log_y=False, range_x=None, range_y=None, points=None, facet_col_wrap=0)
