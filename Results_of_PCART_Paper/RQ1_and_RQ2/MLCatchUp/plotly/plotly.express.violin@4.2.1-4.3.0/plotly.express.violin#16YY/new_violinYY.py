import plotly.express as px
df = px.data.tips()
fig = px.violin(df, None, 'total_bill', None, None, facet_col_wrap=0)
