import dask.dataframe as dd
import pandas as pd
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
ddf1 = dd.from_pandas(df1, npartitions=1)
ddf2 = dd.from_pandas(df2, npartitions=1)
result = dd.concat([ddf1, ddf2], 0, join='outer', interleave_partitions=False, ignore_order=False)
