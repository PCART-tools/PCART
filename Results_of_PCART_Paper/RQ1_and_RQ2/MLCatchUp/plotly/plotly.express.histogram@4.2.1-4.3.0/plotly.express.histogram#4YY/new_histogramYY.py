import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', facet_col_wrap=0)
