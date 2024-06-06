import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, 'year', 'lifeExp', None, None, None, None, hover_data=None, custom_data=None, text=None, facet_col_wrap=0)
