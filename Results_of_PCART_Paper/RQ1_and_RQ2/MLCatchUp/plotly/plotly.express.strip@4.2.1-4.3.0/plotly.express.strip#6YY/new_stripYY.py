import plotly.express as px
df = px.data.tips()
fig = px.strip(data_frame=df, x='total_bill', facet_col_wrap=0)
