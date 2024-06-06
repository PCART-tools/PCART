import plotly.express as px
df = px.data.tips()
fig = px.violin(df, None, 'total_bill', None, None, None, None, None, None, None, None, category_orders={}, labels={}, color_discrete_sequence=None, facet_col_wrap=0)
