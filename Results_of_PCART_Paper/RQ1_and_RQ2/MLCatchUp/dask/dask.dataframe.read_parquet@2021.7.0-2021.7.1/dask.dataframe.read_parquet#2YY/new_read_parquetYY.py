import dask.dataframe as dd
ddf = dd.read_parquet(path='/home/zhang/Documents/example.parquet', aggregate_files=None)
