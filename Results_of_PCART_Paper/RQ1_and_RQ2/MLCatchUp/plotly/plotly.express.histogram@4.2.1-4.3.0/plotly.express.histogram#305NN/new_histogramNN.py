import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, None, None, None, None, None, None, None, {}, {}, None, {}, None, None, 'v', 'relative', None, None, log_x=False, log_y=False, range_x=None, range_y=None, facet_col_wrap=0)
