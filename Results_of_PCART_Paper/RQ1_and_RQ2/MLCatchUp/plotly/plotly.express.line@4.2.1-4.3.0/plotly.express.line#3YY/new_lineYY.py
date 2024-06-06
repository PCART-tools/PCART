import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(data_frame=df, facet_col_wrap=0)
