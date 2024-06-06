import polars as pl
a = pl.col('fruits')
a.str.starts_with(prefix='app')
