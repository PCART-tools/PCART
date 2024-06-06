import dask.array as da
x = da.ones((1, 10, 1, 5), chunks=(1, 5, 1, 5))
x_squeezed = x.squeeze(axis=None)
