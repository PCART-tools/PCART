import polars as pl
a = pl.col('fruits')
a.str.ends_with('go')
