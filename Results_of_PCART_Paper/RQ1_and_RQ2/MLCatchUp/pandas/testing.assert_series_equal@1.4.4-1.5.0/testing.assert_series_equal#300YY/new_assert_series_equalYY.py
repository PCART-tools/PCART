from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(check_flags=True, check_less_precise=False, rtol=1e-05, check_exact=False, atol=1e-08, check_categorical=True, check_dtype=True, obj='Series', left=a, check_freq=True, check_series_type=True, right=b, check_category_order=True, check_index=True, check_index_type='equiv', check_names=True, check_datetimelike_compat=False)
