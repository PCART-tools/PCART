import plotly.express as px
df = px.data.tips()
fig = px.violin(data_frame=df, x=None, y='total_bill', color=None, facet_row=None, facet_col=None, hover_name=None, hover_data=None, custom_data=None, facet_col_wrap=0)
