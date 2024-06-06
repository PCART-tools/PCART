import plotly.express as px
df = px.data.tips()
fig = px.box(df, 'time', 'total_bill', None, None, None, None, None, None, None, None, {}, {}, None, {}, 'v', 'group', False, False, None, range_y=None, points=None, notched=False, title=None, template=None, width=None, height=None, facet_col_wrap=0)
