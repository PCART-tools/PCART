import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, None, None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None, facet_col_spacing=None, pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)
