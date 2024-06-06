import plotly.express as px
df = px.data.gapminder()
fig = px.area(facet_col_wrap=0)
