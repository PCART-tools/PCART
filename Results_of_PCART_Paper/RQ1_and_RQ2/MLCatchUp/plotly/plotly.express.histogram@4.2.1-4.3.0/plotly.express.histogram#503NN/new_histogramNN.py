import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, None, None, None, None, None, None, None, {}, {}, None, {}, None, None, 'v', 'relative', None, None, False, False, None, None, None, cumulative=None, nbins=None, title=None, template=None, width=None, height=None, facet_col_wrap=0)
