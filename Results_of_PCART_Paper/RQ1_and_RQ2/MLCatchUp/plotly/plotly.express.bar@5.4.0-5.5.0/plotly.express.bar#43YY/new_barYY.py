import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_frame=data_canada, x='year', y='pop', color=None, pattern_shape=None, facet_row=None, facet_col=None, facet_col_wrap=0, text_auto=False)
