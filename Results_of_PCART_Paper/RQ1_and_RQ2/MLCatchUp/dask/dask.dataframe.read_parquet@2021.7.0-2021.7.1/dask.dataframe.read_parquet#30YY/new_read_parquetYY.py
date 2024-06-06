import dask.dataframe as dd
ddf = dd.read_parquet('/home/zhang/Documents/example.parquet', None, None, None, None, storage_options=None, engine='auto', aggregate_files=None)
