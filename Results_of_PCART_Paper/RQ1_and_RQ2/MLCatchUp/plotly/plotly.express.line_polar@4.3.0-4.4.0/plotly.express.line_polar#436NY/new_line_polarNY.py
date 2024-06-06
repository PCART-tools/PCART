import plotly.express as px
df = px.data.wind()
fig = px.line_polar(df, 'frequency', 'direction', 'strength', None, None, None, None, None, None, None, None, {}, {}, None, {}, None, {}, 'clockwise', 90, False, None, 'auto', None, False, None, None, None, None, range_theta=None)
