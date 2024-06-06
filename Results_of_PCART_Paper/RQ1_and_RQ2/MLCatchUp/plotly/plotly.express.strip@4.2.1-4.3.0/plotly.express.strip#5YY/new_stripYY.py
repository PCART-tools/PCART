import plotly.express as px
df = px.data.tips()
fig = px.strip(df, x='total_bill', facet_col_wrap=0)
