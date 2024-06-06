import polars as pl
df = pl.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]})
shifted_df = df.shift_and_fill(periods=1, fill_value=0)
