import plotly.express as px
df = px.data.gapminder()
fig = px.area(df, 'year', y='pop', facet_col_wrap=0)
