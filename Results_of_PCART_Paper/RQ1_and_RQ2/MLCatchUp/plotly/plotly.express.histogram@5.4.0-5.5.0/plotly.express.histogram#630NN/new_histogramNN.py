import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, None, None, None, None, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'relative', None, None, False, False, None, None, None, None, None, None, template=None, text_auto=False)
