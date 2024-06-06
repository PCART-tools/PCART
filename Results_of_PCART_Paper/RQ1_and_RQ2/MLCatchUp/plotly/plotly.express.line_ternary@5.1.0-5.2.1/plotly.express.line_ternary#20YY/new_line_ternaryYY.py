import plotly.express as px
df = px.data.election()
fig = px.line_ternary(df, a='Joly', b='Coderre', c='Bergeron', color=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
