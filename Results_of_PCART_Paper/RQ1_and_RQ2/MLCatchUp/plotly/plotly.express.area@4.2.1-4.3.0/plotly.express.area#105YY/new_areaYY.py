import plotly.express as px
df = px.data.gapminder()
fig = px.area(data_frame=df, x='year', y='pop', line_group='country', color='continent', hover_name=None, hover_data=None, custom_data=None, text=None, facet_row=None, facet_col=None, animation_frame=None, animation_group=None, facet_col_wrap=0)
