import polars as pl
pl.col('a').clip(1, upper_bound=10)
