import polars as pl
pl.col('foo').reshape(dimensions=(3, 3))
