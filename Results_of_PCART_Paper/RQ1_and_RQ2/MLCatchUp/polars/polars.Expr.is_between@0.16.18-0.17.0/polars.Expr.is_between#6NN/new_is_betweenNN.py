import polars as pl
pl.col('num').is_between(2, closed='both', upper_bound=4)
