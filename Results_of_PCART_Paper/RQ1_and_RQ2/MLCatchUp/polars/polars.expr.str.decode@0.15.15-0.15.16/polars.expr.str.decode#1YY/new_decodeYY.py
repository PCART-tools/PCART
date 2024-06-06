import polars as pl
df = pl.DataFrame({'strings': ['aGVsbG8gd29ybGQ=', 'cG9sYXJzIGlzIGF3ZXNvbWU=']})
a = pl.col('strings')
df_decoded = df.with_column(a.str.decode('base64'))
