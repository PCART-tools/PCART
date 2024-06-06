import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x='year', facet_col_wrap=0)
