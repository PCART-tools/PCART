import plotly.express as px
df = px.data.tips()
fig = px.histogram(facet_col_wrap=0)
