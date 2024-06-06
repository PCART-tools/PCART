import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, None, text_auto=False)
