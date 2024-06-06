from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a, check_flags=True, check_datetimelike_compat=False, check_index=True, check_series_type=True, check_names=True, check_category_order=True, right=b, check_exact=False, check_freq=True, check_dtype=True, check_categorical=True, check_index_type='equiv', check_less_precise=False, rtol=1e-05)
