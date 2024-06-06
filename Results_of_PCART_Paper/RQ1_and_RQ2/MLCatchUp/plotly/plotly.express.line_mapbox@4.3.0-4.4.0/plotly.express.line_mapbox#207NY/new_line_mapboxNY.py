import pandas as pd
us_cities = pd.read_csv('/home/zhang/Documents/us-cities-top-1k.csv')
us_cities = us_cities.query("State in ['New York', 'Ohio']")
import plotly.express as px
fig = px.line_mapbox(us_cities, 'lat', 'lon', 'State', None, None, None, None, None, None, None, {}, {}, None, {}, 8, None, None, width=None, height=None, center=None, mapbox_style=None)
