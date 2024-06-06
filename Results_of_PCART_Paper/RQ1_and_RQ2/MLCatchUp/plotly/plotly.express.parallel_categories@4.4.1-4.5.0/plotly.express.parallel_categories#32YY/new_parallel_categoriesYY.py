import plotly.express as px
df = px.data.tips()
fig = px.parallel_categories(df, ['sex', 'smoker', 'day'], 'size', labels={'sex': 'Payer sex', 'smoker': 'Smokers at the table', 'day': 'Day of week'}, color_continuous_scale=px.colors.sequential.Inferno, range_color=None, color_continuous_midpoint=None, dimensions_max_cardinality=50)
