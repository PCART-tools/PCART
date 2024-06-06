import dask.dataframe as dd
ddf = dd.read_parquet('/home/zhang/Documents/example.parquet', columns=None, chunksize=None)
