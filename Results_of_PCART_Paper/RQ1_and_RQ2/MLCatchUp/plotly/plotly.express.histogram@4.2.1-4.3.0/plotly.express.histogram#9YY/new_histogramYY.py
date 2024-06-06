import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, x='total_bill', y=None, facet_col_wrap=0)
