import plotly.express as px
df = px.data.tips()
fig = px.violin(df, facet_col_wrap=0)
