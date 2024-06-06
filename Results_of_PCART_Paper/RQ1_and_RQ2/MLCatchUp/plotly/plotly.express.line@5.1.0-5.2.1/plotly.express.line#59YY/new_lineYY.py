import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, 'year', 'lifeExp', None, None, line_dash=None, hover_name=None, hover_data=None, custom_data=None, text=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
