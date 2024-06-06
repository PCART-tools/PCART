import dask.dataframe as dd
ddf = dd.read_parquet(path='/home/zhang/Documents/example.parquet', columns=None, filters=None, categories=None, index=None, storage_options=None, chunksize=None)
