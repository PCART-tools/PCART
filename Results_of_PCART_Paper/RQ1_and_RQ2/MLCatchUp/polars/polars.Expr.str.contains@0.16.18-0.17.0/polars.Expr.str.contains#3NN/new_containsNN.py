import polars as pl
a = pl.col('s')
default_match = a.str.contains('AA', literal=False)
