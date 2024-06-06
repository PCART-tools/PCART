import dask.dataframe as dd
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1], 'C': [2, 3, 4, 5, 6]})
ddf = dd.from_pandas(df, npartitions=2)
ddf = ddf.drop('B', axis=1, errors='raise', columns=None)
