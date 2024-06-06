import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, 'year', 'pop', None, None, None, None, None, None, None, None, error_x_minus=None, error_y=None, error_y_minus=None, facet_col_wrap=0)
