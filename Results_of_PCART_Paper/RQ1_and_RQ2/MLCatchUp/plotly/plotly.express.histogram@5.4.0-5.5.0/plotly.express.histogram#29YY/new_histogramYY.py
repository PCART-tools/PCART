import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, None, None, facet_row=None, facet_col=None, text_auto=False)
