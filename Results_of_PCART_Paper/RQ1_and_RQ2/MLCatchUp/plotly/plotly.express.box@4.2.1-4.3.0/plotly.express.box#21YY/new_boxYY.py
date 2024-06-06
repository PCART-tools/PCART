import plotly.express as px
df = px.data.tips()
fig = px.box(data_frame=df, x='time', y='total_bill', color=None, facet_row=None, facet_col_wrap=0)
