import plotly.express as px
df = px.data.gapminder().query("country=='Brazil'")
fig = px.line_3d(data_frame=df, x='gdpPercap', y='pop', z='year', color=None, line_dash=None, text=None, line_group=None, hover_name=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
