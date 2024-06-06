import polars as pl
df = pl.DataFrame({'foo': [1, 2, 3], 'bar': [4, 5, 6]})
s = pl.Series([10, 20, 30])
df.replace('foo',  s)
