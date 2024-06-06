import dask.dataframe as dd
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3, None, 5], 'B': [5, None, 3, 2, 1], 'C': [None, 2, 3, 4, 5]})
ddf = dd.from_pandas(df, npartitions=2)
ddf_dropped_rows = ddf.dropna('any', None, thresh=None)
