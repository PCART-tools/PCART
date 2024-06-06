import plotly.express as px
df = px.data.wind()
fig = px.line_polar(df, 'frequency', 'direction', 'strength', None, None, None, None, None, None, None, None, {}, {}, None, {}, None, {}, 'clockwise', start_angle=90, line_close=False, line_shape=None, render_mode='auto', range_r=None, log_r=False, title=None, template=None, width=None, range_theta=None)
