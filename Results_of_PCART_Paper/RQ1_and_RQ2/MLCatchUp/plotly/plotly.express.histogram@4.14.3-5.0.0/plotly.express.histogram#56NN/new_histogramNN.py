import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, None, None, None, 0, None, facet_col_spacing=None, hover_name=None, pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)
