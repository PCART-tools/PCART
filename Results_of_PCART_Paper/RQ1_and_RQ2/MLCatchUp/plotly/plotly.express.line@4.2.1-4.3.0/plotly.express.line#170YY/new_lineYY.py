import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x='year', y='lifeExp', line_group=None, color=None, line_dash=None, hover_name=None, hover_data=None, custom_data=None, text=None, facet_row=None, facet_col=None, error_x=None, error_x_minus=None, error_y=None, error_y_minus=None, animation_frame=None, facet_col_wrap=0)
