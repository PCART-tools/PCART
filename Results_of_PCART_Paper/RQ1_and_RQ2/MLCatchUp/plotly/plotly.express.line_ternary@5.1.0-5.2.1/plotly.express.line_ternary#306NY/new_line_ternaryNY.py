import plotly.express as px
df = px.data.election()
fig = px.line_ternary(df, 'Joly', 'Coderre', 'Bergeron', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, line_shape=None, title=None, template=None, width=None, height=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
