import plotly.express as px
df = px.data.tips()
fig = px.box(df, x='time', y='total_bill', facet_col_wrap=0)
