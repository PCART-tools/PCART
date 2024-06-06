import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, facet_col_wrap=0)
