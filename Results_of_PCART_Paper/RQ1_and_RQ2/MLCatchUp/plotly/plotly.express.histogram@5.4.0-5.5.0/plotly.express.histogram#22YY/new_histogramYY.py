import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, None, pattern_shape=None, facet_row=None, text_auto=False)
