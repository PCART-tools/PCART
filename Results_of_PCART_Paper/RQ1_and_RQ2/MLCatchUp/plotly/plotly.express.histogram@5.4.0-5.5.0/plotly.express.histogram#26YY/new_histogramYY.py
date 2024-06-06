import plotly.express as px
df = px.data.tips()
fig = px.histogram(data_frame=df, x='total_bill', y=None, color=None, pattern_shape=None, facet_row=None, text_auto=False)
