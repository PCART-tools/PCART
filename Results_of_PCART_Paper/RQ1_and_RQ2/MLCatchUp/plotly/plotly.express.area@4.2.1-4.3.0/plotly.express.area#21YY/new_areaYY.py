import plotly.express as px
df = px.data.gapminder()
fig = px.area(data_frame=df, x='year', y='pop', line_group='country', color='continent', facet_col_wrap=0)
