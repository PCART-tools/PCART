import plotly.express as px
df = px.data.tips()
fig = px.strip(df, 'total_bill', 'day', None, None, None, None, None, None, None, None, {}, {}, None, {}, 'v', 'group', False, False, None, None, title=None, template=None, facet_col_wrap=0)
