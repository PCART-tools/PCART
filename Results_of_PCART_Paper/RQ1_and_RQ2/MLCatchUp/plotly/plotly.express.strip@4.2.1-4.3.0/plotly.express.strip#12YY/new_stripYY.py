import plotly.express as px
df = px.data.tips()
fig = px.strip(df, 'total_bill', 'day', color=None, facet_col_wrap=0)
