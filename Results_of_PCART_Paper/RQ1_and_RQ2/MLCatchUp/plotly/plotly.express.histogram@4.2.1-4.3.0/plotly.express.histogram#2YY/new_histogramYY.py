import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, facet_col_wrap=0)
