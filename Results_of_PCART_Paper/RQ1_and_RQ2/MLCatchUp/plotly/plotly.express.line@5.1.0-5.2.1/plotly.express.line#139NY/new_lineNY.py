import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, 'year', 'lifeExp', None, None, None, None, None, None, None, None, None, facet_col_wrap=0, facet_row_spacing=None, facet_col_spacing=None, error_x=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
