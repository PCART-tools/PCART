import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, 'year', 'lifeExp', None, None, None, None, None, None, text=None, facet_row=None, facet_col=None, error_x=None, error_x_minus=None, error_y=None, facet_col_wrap=0)
