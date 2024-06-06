import plotly.express as px
df = px.data.gapminder().query("country=='Brazil'")
fig = px.line_3d(df, 'gdpPercap', 'pop', 'year', None, None, None, None, hover_name=None, hover_data=None, custom_data=None, error_x=None, error_x_minus=None, error_y=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
