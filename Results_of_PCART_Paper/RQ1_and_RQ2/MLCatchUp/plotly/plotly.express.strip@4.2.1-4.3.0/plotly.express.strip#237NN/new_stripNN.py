import plotly.express as px
df = px.data.tips()
fig = px.strip(df, 'total_bill', 'day', None, None, None, None, None, None, None, None, {}, {}, None, {}, 'v', stripmode='group', log_x=False, log_y=False, range_x=None, range_y=None, facet_col_wrap=0)
