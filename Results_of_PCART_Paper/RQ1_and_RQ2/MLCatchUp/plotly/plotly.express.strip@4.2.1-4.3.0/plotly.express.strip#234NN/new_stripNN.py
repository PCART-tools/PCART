import plotly.express as px
df = px.data.tips()
fig = px.strip(df, 'total_bill', 'day', None, None, None, None, None, None, None, None, {}, {}, None, {}, 'v', 'group', False, False, range_x=None, range_y=None, facet_col_wrap=0)
