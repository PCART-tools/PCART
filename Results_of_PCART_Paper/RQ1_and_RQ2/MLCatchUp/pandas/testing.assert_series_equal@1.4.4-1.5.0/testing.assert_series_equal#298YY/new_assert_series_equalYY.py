from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a, check_index_type='equiv', check_series_type=True, check_exact=False, check_names=True, check_categorical=True, obj='Series', check_flags=True, check_category_order=True, check_dtype=True, check_datetimelike_compat=False, check_less_precise=False, check_index=True, check_freq=True, right=b, rtol=1e-05, atol=1e-08)
