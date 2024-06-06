import dask.array as da
random_integers = da.random.randint(0, 100, (1000, 1000), dtype='l')
