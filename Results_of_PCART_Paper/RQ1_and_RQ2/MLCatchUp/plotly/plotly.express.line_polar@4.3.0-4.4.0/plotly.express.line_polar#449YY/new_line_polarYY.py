import plotly.express as px
df = px.data.wind()
fig = px.line_polar(df, 'frequency', 'direction', 'strength', None, None, None, None, None, None, None, None, {}, {}, None, {}, line_dash_sequence=None, line_dash_map={}, direction='clockwise', start_angle=90, line_close=False, line_shape=None, render_mode='auto', range_r=None, log_r=False, title=None, template=None, width=None, height=None, range_theta=None)
