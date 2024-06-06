import polars as pl
df = pl.DataFrame({'a': [1.5, 2, float('NaN'), 4], 'b': [0.5, 4, float('NaN'), 13]})
df.fill_nan(value=99)
