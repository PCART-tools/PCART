import plotly.express as px
df = px.data.election()
fig = px.line_ternary(data_frame=df, a='Joly', symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
