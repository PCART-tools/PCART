import plotly.express as px
df = px.data.tips()
fig = px.parallel_categories(df, ['sex', 'smoker', 'day'], 'size', labels={'sex': 'Payer sex', 'smoker': 'Smokers at the table', 'day': 'Day of week'}, dimensions_max_cardinality=50)
