import plotly.express as px
df = px.data.tips()
fig = px.strip(df, 'total_bill', 'day', None, None, None, None, None, None, None, None, {}, {}, color_discrete_sequence=None, color_discrete_map={}, orientation='v', stripmode='group', log_x=False, log_y=False, facet_col_wrap=0)
