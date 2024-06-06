import plotly.express as px
df = px.data.iris()
fig = px.scatter(data_frame=df, facet_col_wrap=0)
