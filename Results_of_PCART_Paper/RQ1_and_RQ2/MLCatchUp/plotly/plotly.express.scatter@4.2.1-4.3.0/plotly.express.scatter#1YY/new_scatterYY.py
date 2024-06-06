import plotly.express as px
df = px.data.iris()
fig = px.scatter(facet_col_wrap=0)
