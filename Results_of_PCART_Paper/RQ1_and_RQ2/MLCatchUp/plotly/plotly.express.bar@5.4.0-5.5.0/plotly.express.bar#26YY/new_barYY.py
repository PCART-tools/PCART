import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_frame=data_canada, x='year', y='pop', color=None, pattern_shape=None, facet_row=None, text_auto=False)
