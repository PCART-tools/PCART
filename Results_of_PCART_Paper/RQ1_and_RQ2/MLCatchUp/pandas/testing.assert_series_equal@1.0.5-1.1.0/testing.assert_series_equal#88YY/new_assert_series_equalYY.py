import pandas as pd
from pandas._testing import assert_series_equal
df1 = pd.Series({'a': 1, 'b': 1})
df2 = pd.Series({'a': 1, 'b': 1})
assert_series_equal(left=df1, right=df1, check_dtype=True, check_index_type='equiv', check_series_type=True, check_less_precise=False, check_names=True, check_exact=False, check_datetimelike_compat=False, check_categorical=True, check_category_order=True, obj='Series', check_freq=True, rtol=1e-05, atol=1e-08)
