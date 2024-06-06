import dask.array as da
import dask.dataframe as dd
x = da.random.random((10000, 5), chunks=(1000, 5))
ddf = dd.from_dask_array(x, ['A', 'B', 'C', 'D', 'E'], index=None)
