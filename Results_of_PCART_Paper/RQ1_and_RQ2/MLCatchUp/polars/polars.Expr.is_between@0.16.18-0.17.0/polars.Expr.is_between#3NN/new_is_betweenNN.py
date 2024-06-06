import polars as pl
pl.col('num').is_between(lower_bound=2, upper_bound=4)
