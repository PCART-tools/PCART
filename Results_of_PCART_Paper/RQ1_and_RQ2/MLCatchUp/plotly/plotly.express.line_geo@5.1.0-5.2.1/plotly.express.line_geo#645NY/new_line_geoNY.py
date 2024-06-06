import plotly.express as px
df = px.data.gapminder().query('year == 2007')
fig = px.line_geo(df, None, None, 'iso_alpha', None, None, None, 'continent', None, None, None, None, 0, None, None, None, None, None, None, None, None, category_orders=None, labels=None, color_discrete_sequence=None, color_discrete_map=None, line_dash_sequence=None, line_dash_map=None, projection='orthographic', scope=None, center=None, fitbounds=None, basemap_visible=None, title=None, template=None, width=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
