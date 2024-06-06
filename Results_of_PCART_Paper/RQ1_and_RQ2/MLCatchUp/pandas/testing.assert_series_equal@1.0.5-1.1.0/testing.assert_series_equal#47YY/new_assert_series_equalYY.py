import pandas as pd
from pandas._testing import assert_series_equal
df1 = pd.Series({'a': 1, 'b': 1})
df2 = pd.Series({'a': 1, 'b': 1})
assert_series_equal(df1, df1, True, 'equiv', True, check_less_precise=False, check_names=True, check_exact=False, check_datetimelike_compat=False, check_freq=True, rtol=1e-05, atol=1e-08)
