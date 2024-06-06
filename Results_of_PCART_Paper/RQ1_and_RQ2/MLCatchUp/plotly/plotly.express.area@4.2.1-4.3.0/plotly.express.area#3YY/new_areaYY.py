import plotly.express as px
df = px.data.gapminder()
fig = px.area(data_frame=df, facet_col_wrap=0)
