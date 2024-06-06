import polars as pl
pl.col('a').clip(lower_bound=1, upper_bound=10)
