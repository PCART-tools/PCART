import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(facet_col_wrap=0)
