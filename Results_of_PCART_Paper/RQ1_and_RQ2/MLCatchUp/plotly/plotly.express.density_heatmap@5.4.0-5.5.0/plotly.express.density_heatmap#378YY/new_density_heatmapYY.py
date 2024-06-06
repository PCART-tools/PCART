import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(df, 'total_bill', 'tip', None, None, None, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, False, False, None, None, histfunc=None, text_auto=False)
