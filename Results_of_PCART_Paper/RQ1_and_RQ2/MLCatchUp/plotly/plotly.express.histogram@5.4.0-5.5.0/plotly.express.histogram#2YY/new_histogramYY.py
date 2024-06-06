import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', text_auto=False)
