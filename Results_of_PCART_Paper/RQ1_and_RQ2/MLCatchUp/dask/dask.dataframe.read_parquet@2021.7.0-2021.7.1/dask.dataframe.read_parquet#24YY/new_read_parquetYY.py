import dask.dataframe as dd
ddf = dd.read_parquet('/home/zhang/Documents/example.parquet', None, None, categories=None, index=None, storage_options=None, aggregate_files=None)
