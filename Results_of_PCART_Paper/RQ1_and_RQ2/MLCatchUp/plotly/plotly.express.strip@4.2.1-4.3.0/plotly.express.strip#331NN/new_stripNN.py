import plotly.express as px
df = px.data.tips()
fig = px.strip(df, 'total_bill', 'day', None, None, None, None, None, None, None, None, {}, {}, None, {}, 'v', 'group', False, False, None, range_y=None, title=None, template=None, width=None, height=None, facet_col_wrap=0)
