import plotly.express as px
df = px.data.gapminder()
fig = px.area(df, 'year', 'pop', 'country', facet_col_wrap=0)
