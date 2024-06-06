import polars as pl
pl.col('num').is_between(2, upper_bound=4)
