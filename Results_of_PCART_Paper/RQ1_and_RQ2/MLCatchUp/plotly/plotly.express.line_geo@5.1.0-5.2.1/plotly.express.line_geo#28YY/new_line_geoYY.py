import plotly.express as px
df = px.data.gapminder().query('year == 2007')
fig = px.line_geo(data_frame=df, lat=None, lon=None, locations='iso_alpha', locationmode=None, geojson=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
