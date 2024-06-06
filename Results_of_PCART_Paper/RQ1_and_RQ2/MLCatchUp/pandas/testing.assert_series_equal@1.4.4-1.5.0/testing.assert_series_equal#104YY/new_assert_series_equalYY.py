from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(check_series_type=True, check_names=True, check_less_precise=False, check_index=True, check_datetimelike_compat=False, check_exact=False, left=a, check_dtype=True, check_index_type='equiv', right=b)
