import plotly.express as px
df = px.data.wind()
fig = px.line_polar(df, 'frequency', 'direction', 'strength', None, None, None, None, None, None, None, None, None, None, color_discrete_sequence=None, color_discrete_map=None, line_dash_sequence=None, line_dash_map=None, direction='clockwise', start_angle=90, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
