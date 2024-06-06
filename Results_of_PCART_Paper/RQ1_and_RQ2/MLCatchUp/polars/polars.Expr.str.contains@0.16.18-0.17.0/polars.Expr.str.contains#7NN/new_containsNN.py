import polars as pl
a = pl.col('s')
default_match = a.str.contains('AA', strict=True, literal=False)
