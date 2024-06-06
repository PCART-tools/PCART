import dask.dataframe as dd
ddf = dd.read_parquet('/home/zhang/Documents/example.parquet', None, None, None, index=None, storage_options=None, engine='auto', gather_statistics=None, chunksize=None)
