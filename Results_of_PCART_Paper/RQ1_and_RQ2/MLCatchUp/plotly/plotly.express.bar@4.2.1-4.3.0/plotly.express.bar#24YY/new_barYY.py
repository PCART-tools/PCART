import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, 'year', 'pop', None, facet_row=None, facet_col=None, facet_col_wrap=0)
