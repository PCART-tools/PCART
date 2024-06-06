import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, 'year', y='lifeExp', facet_col_wrap=0)
