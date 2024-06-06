import polars as pl
pl.arg_where(pl.col('a') % 2 == 0)
