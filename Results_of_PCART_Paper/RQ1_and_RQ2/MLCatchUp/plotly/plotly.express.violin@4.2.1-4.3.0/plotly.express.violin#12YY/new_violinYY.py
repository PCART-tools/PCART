import plotly.express as px
df = px.data.tips()
fig = px.violin(df, None, 'total_bill', color=None, facet_col_wrap=0)
