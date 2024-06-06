import plotly.express as px
df = px.data.wind()
fig = px.line_polar(df, 'frequency', 'direction', 'strength', None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'clockwise', 90, False, None, 'auto', None, range_theta=None, log_r=False, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
