import plotly.express as px
df = px.data.tips()
fig = px.violin(df, None, y='total_bill', facet_col_wrap=0)
