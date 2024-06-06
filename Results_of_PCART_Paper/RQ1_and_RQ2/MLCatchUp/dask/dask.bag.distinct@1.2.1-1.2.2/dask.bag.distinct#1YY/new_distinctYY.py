import dask.bag as db
b = db.from_sequence([1, 2, 3, 1, 2, 3, 4, 5, 5, 6])
distinct_b = b.distinct(key=None)
