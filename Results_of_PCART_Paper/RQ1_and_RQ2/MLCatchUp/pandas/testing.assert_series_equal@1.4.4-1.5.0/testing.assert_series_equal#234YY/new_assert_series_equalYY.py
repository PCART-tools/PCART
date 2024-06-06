from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(check_dtype=True, left=a, check_series_type=True, right=b, check_category_order=True, check_names=True, check_categorical=True, check_exact=False, check_flags=True, check_freq=True, rtol=1e-05, check_index_type='equiv', check_datetimelike_compat=False, check_less_precise=False, check_index=True)
