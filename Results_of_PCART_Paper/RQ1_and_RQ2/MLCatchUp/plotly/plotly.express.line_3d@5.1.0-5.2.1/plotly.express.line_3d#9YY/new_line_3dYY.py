import plotly.express as px
df = px.data.gapminder().query("country=='Brazil'")
fig = px.line_3d(df, x='gdpPercap', y='pop', symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
