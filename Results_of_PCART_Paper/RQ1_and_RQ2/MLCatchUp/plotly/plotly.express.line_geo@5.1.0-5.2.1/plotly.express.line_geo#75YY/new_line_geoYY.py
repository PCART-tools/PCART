import plotly.express as px
df = px.data.gapminder().query('year == 2007')
fig = px.line_geo(df, None, None, locations='iso_alpha', locationmode=None, geojson=None, featureidkey=None, color='continent', line_dash=None, text=None, facet_row=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
