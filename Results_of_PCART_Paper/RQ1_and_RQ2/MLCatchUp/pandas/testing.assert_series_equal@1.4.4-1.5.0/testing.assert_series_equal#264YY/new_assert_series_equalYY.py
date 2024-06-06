from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a, check_flags=True, right=b, check_index_type='equiv', check_names=True, check_datetimelike_compat=False, check_dtype=True, check_exact=False, atol=1e-08, check_categorical=True, rtol=1e-05, check_freq=True, check_series_type=True, check_index=True, check_category_order=True, check_less_precise=False)
