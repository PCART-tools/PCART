import plotly.express as px
df = px.data.wind()
fig = px.line_polar(data_frame=df, r='frequency', theta='direction', color='strength', line_dash=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
