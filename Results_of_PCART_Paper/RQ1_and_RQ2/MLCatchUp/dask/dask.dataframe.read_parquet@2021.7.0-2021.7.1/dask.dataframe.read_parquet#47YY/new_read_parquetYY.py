import dask.dataframe as dd
ddf = dd.read_parquet('/home/zhang/Documents/example.parquet', None, None, None, None, None, 'auto', gather_statistics=None, split_row_groups=None, aggregate_files=None)
