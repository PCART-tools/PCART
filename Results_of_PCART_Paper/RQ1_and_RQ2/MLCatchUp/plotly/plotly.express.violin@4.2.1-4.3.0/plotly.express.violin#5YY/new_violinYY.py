import plotly.express as px
df = px.data.tips()
fig = px.violin(df, x=None, facet_col_wrap=0)
