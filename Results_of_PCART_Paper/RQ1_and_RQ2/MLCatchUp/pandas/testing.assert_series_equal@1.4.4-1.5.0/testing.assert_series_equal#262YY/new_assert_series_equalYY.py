from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a,  b, check_category_order=True, rtol=1e-05, check_names=True, atol=1e-08, check_datetimelike_compat=False, check_flags=True, check_less_precise=False, check_index=True, check_dtype=True, check_categorical=True, check_series_type=True, check_freq=True, check_index_type='equiv', check_exact=False)
