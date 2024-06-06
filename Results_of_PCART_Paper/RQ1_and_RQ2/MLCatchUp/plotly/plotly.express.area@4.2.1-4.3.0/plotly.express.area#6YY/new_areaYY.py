import plotly.express as px
df = px.data.gapminder()
fig = px.area(data_frame=df, x='year', facet_col_wrap=0)
