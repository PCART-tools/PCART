import polars as pl
pl.arg_where(condition=pl.col('a') % 2 == 0)
