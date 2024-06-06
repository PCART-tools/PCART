import plotly.express as px
df = px.data.tips()
fig = px.strip(df, 'total_bill', 'day', None, None, None, None, None, None, None, None, {}, labels={}, color_discrete_sequence=None, color_discrete_map={}, orientation='v', facet_col_wrap=0)
