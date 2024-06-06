import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, 'year', y='pop', color=None, facet_row=None, facet_col=None, hover_name=None, facet_col_wrap=0)
