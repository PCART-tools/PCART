import plotly.express as px
df = px.data.gapminder().query('year == 2007')
fig = px.line_geo(df, None, None, 'iso_alpha', None, None, None, 'continent', None, None, None, None, 0, None, None, None, None, None, None, None, None, None, labels=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
