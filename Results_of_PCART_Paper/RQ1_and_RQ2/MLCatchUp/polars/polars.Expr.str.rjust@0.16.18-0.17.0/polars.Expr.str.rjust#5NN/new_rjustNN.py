import polars as pl
df = pl.DataFrame({'text': ['foo', 'bar', 'baz']})
context = pl.col('text')
rjust_df = df.select(context.str.rjust(width=10, fillchar='-'))
