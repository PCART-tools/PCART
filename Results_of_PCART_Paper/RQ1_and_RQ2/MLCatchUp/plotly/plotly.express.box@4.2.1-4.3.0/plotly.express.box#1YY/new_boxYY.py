import plotly.express as px
df = px.data.tips()
fig = px.box(facet_col_wrap=0)
