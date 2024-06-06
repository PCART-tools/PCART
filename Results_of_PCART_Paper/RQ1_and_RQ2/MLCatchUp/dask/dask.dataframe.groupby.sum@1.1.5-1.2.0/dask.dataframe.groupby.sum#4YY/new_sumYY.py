import dask.dataframe as dd
import pandas as pd
from inspect import getfile, signature
pdf = pd.DataFrame({'category': ['A', 'B', 'A', 'B', 'B', 'A', 'A', 'A'], 'values': [1, 2, 3, 4, 5, 6, 7, 8]})
ddf = dd.from_pandas(pdf, npartitions=2)
result = ddf.groupby('category').sum(None, 1, min_count=None)
