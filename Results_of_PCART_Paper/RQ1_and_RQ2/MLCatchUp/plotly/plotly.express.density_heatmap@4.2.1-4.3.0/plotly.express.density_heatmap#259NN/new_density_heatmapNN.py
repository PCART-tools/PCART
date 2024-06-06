import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(df, 'total_bill', 'tip', None, None, None, None, None, None, None, {}, {}, None, None, None, None, None, opacity=None, log_x=False, log_y=False, range_x=None, range_y=None, facet_col_wrap=0)
