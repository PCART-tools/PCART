import plotly.express as px
df = px.data.tips()
fig = px.density_contour(data_frame=df, x='total_bill', y='tip', z=None, color=None, facet_row=None, facet_col=None, facet_col_wrap=0)
