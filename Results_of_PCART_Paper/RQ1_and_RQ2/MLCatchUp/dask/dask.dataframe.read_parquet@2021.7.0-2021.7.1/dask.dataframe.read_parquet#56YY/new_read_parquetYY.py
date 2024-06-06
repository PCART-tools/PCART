import dask.dataframe as dd
ddf = dd.read_parquet('/home/zhang/Documents/example.parquet', None, None, None, None, None, 'auto', None, None, read_from_paths=None, aggregate_files=None)
