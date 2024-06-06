import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, 'year', 'lifeExp', None, None, None, None, None, None, None, None, None, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, line_dash_sequence=None, line_dash_map=None, log_x=False, log_y=False, range_x=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
