import plotly.express as px
df = px.data.carshare()
fig = px.scatter_mapbox(df, 'centroid_lat', lon='centroid_lon', center=None, mapbox_style=None)
