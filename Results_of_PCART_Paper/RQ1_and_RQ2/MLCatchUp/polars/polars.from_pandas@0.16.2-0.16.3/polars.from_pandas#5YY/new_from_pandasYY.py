import polars as pl
import pandas as pd
pdf = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': ['a', 'b', 'c', 'd', 'e']})
df = pl.from_pandas(df=pdf, rechunk=True)
