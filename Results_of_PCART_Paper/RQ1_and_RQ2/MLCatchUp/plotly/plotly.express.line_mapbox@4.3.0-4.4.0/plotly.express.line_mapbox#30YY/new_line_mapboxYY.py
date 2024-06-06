import pandas as pd
us_cities = pd.read_csv('/home/zhang/Documents/us-cities-top-1k.csv')
us_cities = us_cities.query("State in ['New York', 'Ohio']")
import plotly.express as px
fig = px.line_mapbox(data_frame=us_cities, lat='lat', lon='lon', color='State', text=None, hover_name=None, hover_data=None, center=None, mapbox_style=None)
