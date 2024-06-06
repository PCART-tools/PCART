import plotly.express as px
df = px.data.gapminder().query("country=='Brazil'")
fig = px.line_3d(df, 'gdpPercap', 'pop', 'year', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, False, log_y=False, log_z=False, range_x=None, range_y=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
