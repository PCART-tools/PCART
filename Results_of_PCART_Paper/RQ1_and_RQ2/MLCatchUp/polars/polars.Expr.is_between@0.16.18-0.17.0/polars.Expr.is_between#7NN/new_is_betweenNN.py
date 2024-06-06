import polars as pl
pl.col('num').is_between(closed='both', lower_bound=2, upper_bound=4)
