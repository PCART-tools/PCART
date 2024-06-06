import plotly.express as px
df = px.data.carshare()
fig = px.scatter_mapbox(df, lat='centroid_lat', lon='centroid_lon', color='peak_hour', text=None, hover_name=None, hover_data=None, center=None, mapbox_style=None)
