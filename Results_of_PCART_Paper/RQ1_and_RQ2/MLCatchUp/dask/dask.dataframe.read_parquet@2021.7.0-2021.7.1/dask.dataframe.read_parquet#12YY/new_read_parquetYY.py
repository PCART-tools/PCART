import dask.dataframe as dd
ddf = dd.read_parquet('/home/zhang/Documents/example.parquet', None, filters=None, categories=None, aggregate_files=None)
