import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, None, None, None, 0, None, None, None, None, None, None, None, None, color_discrete_sequence=None, color_discrete_map=None, marginal=None, pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)
