import polars as pl
df = pl.DataFrame({'text': ['   hello ', ' world   ', '   !   ']})
context = pl.col('text')
df_with_stripped_text = df.select(context.str.strip(None))
