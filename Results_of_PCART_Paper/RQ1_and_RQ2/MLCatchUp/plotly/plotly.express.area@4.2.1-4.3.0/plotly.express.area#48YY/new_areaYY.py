import plotly.express as px
df = px.data.gapminder()
fig = px.area(df, 'year', 'pop', 'country', 'continent', None, None, custom_data=None, text=None, facet_col_wrap=0)
