import plotly.express as px
df = px.data.tips()
fig = px.density_contour(df, x='total_bill', y='tip', facet_col_wrap=0)
