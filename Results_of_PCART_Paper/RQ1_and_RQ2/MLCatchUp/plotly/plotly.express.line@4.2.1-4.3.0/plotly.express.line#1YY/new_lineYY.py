import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(facet_col_wrap=0)
