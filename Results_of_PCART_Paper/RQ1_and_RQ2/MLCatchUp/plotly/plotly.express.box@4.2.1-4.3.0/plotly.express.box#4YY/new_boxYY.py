import plotly.express as px
df = px.data.tips()
fig = px.box(df, 'time', facet_col_wrap=0)
