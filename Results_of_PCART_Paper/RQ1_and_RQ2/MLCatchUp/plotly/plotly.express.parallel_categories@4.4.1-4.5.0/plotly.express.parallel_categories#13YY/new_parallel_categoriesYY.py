import plotly.express as px
df = px.data.tips()
fig = px.parallel_categories(df, dimensions=['sex', 'smoker', 'day'], color='size', labels={'sex': 'Payer sex', 'smoker': 'Smokers at the table', 'day': 'Day of week'}, dimensions_max_cardinality=50)
