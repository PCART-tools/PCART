import plotly.express as px
df = px.data.election()
fig = px.line_ternary(df, 'Joly', 'Coderre', 'Bergeron', None, None, None, None, hover_data=None, custom_data=None, text=None, animation_frame=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
