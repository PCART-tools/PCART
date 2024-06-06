import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, 'year', 'pop', None, None, None, None, None, None, None, None, None, None, None, None, None, {}, {}, None, {}, None, range_color=None, color_continuous_midpoint=None, opacity=None, orientation='v', barmode='relative', log_x=False, log_y=False, facet_col_wrap=0)
