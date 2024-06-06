import plotly.express as px
df = px.data.election()
fig = px.line_ternary(df, 'Joly', b='Coderre', c='Bergeron', color=None, line_dash=None, line_group=None, hover_name=None, hover_data=None, custom_data=None, text=None, animation_frame=None, animation_group=None, category_orders=None, labels=None, color_discrete_sequence=None, color_discrete_map=None, line_dash_sequence=None, line_dash_map=None, line_shape=None, title=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
