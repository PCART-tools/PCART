import plotly.express as px
df = px.data.gapminder().query("country=='Brazil'")
fig = px.line_3d(df, 'gdpPercap', 'pop', 'year', color=None, line_dash=None, text=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
