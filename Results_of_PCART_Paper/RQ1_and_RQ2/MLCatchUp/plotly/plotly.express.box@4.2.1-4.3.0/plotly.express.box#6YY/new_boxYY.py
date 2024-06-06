import plotly.express as px
df = px.data.tips()
fig = px.box(data_frame=df, x='time', facet_col_wrap=0)
