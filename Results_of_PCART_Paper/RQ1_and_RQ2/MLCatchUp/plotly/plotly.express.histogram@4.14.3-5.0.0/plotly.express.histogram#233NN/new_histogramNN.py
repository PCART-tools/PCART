import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, None, None, None, 0, None, None, None, None, None, None, None, None, None, None, None, opacity=None, orientation=None, barmode='relative', pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)
