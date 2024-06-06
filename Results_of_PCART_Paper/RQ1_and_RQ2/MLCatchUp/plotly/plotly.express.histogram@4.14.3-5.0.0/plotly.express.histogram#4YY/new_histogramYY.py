import plotly.express as px
df = px.data.tips()
fig = px.histogram(data_frame=df, x='total_bill', pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)
