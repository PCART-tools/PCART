import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, color=None, pattern_shape=None, text_auto=False)
