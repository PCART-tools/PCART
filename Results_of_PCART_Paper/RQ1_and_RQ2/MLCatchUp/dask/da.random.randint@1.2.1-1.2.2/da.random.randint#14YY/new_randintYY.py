import dask.array as da
random_integers = da.random.randint(low=0, high=100, size=(1000, 1000), chunks=(100, 100), dtype='l')
