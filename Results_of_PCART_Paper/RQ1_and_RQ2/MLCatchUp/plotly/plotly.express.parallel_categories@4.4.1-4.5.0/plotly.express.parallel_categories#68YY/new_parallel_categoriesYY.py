import plotly.express as px
df = px.data.tips()
fig = px.parallel_categories(df, ['sex', 'smoker', 'day'], 'size', {'sex': 'Payer sex', 'smoker': 'Smokers at the table', 'day': 'Day of week'}, px.colors.sequential.Inferno, None, None, None, None, width=None, height=None, dimensions_max_cardinality=50)
