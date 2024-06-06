import plotly.express as px
df = px.data.tips()
fig = px.strip(data_frame=df, x='total_bill', y='day', color=None, facet_row=None, facet_col=None, hover_name=None, facet_col_wrap=0)
