import plotly.express as px
df = px.data.tips()
fig = px.strip(facet_col_wrap=0)
