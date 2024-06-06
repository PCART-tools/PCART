import plotly.express as px
df = px.data.tips()
fig = px.strip(df, facet_col_wrap=0)
