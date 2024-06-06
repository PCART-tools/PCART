import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(df, 'total_bill', 'tip', None, None, None, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, False, log_y=False, range_x=None, range_y=None, histfunc=None, histnorm=None, nbinsx=None, text_auto=False)
