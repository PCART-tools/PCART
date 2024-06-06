import dask.dataframe as dd
import pandas as pd
df = pd.DataFrame({'A': range(100), 'B': range(100, 200)})
ddf = dd.from_pandas(df, npartitions=5)
ddf_repartitioned = ddf.repartition(divisions=None, npartitions=10, freq=None, partition_size=None)
