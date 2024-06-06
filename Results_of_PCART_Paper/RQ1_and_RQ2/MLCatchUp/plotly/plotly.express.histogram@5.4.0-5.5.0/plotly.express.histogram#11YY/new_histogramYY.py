import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', y=None, color=None, text_auto=False)
