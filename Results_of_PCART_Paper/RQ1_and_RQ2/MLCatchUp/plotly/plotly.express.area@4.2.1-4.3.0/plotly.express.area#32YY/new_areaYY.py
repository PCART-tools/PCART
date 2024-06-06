import plotly.express as px
df = px.data.gapminder()
fig = px.area(df, 'year', 'pop', 'country', color='continent', hover_name=None, hover_data=None, facet_col_wrap=0)
