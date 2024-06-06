import polars as pl
pl.col('num').is_between(2,  4, closed='both')
