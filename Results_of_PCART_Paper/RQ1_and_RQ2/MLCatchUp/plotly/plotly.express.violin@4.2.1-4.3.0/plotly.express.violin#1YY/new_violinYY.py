import plotly.express as px
df = px.data.tips()
fig = px.violin(facet_col_wrap=0)
