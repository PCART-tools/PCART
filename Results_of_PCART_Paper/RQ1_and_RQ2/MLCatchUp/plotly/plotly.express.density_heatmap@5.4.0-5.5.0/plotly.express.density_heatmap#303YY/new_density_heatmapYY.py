import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(df, 'total_bill', 'tip', None, None, None, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, marginal_y=None, opacity=None, log_x=False, log_y=False, text_auto=False)
