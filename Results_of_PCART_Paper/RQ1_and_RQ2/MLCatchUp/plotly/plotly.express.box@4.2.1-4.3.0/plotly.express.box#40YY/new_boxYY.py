import plotly.express as px
df = px.data.tips()
fig = px.box(df, 'time', 'total_bill', None, None, facet_col=None, hover_name=None, hover_data=None, facet_col_wrap=0)
