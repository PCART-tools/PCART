import polars as pl
df = pl.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1], 'C': [2, 3, 4, 5, 6]})
df_dropped = df.drop('B')
