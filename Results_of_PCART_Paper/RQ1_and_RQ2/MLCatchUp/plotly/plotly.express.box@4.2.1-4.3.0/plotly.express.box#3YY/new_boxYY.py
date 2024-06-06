import plotly.express as px
df = px.data.tips()
fig = px.box(data_frame=df, facet_col_wrap=0)
