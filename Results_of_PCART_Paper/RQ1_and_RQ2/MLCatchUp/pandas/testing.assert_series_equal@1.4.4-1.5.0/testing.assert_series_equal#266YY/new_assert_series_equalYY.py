from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(atol=1e-08, check_category_order=True, left=a, check_flags=True, check_series_type=True, check_categorical=True, check_less_precise=False, check_exact=False, check_datetimelike_compat=False, check_names=True, check_dtype=True, check_index_type='equiv', rtol=1e-05, right=b, check_index=True, check_freq=True)
