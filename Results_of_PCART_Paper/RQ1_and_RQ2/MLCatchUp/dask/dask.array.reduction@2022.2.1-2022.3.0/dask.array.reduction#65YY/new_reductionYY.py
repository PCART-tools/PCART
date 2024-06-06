import dask.array as da
import numpy as np

def chunk_sum_of_squares(chunk, axis=None, keepdims=False, dtype=None):
    sum_squares = np.sum(chunk ** 2, axis=axis, keepdims=keepdims)
    return sum_squares.reshape(-1, 1) if keepdims else sum_squares
x = da.random.random(size=(10000, 1000), chunks=(1000, 1000))
result = da.reduction(x, chunk_sum_of_squares, np.sum, None, True, dtype=x.dtype, split_every=None, combine=np.sum, name=None, out=None, concatenate=True, output_size=1, weights=None)
