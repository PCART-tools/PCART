import plotly.express as px
df = px.data.wind()
fig = px.line_polar(df, 'frequency', 'direction', color='strength', line_dash=None, hover_name=None, hover_data=None, custom_data=None, line_group=None, text=None, animation_frame=None, animation_group=None, category_orders=None, labels=None, color_discrete_sequence=None, color_discrete_map=None, line_dash_sequence=None, line_dash_map=None, direction='clockwise', symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
