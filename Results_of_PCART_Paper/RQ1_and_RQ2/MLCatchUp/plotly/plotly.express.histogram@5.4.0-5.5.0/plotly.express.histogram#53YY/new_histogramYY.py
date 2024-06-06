import plotly.express as px
df = px.data.tips()
fig = px.histogram(data_frame=df, x='total_bill', y=None, color=None, pattern_shape=None, facet_row=None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None, text_auto=False)
