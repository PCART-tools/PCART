import plotly.express as px
df = px.data.carshare()
fig = px.scatter_mapbox(df, 'centroid_lat', 'centroid_lon', 'peak_hour', None, None, None, None, None, None, None, {}, {}, None, {}, None, None, None, None, None, zoom=8, title=None, template=None, width=None, center=None, mapbox_style=None)
