import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, None, None, None, None, None, None, None, {}, {}, None, {}, marginal=None, opacity=None, orientation='v', barmode='relative', facet_col_wrap=0)
