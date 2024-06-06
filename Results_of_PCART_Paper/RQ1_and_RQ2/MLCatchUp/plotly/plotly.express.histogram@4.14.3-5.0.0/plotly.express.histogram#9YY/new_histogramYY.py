import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, None, pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)
