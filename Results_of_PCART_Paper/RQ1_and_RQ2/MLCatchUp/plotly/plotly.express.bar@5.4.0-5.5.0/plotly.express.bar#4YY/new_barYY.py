import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_frame=data_canada, x='year', text_auto=False)
