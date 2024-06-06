import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, 'year', 'pop', None, None, None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None, facet_col_spacing=None, text_auto=False)
