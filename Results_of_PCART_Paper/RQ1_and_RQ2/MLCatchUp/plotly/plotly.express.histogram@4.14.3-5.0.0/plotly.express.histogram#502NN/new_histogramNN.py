import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, None, None, None, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, 'relative', None, None, False, log_y=False, range_x=None, range_y=None, histfunc=None, cumulative=None, nbins=None, title=None, pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)
