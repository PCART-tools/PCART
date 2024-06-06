import plotly.express as px
df = px.data.tips()
fig = px.violin(df, None, y='total_bill', color=None, facet_row=None, facet_col=None, hover_name=None, facet_col_wrap=0)
