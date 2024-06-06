import dask.dataframe as dd
import pandas as pd
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'], 'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three']})
ddf = dd.from_pandas(df, npartitions=3)
ddf_unique = ddf.drop_duplicates(None, split_out=1, subset=None)
