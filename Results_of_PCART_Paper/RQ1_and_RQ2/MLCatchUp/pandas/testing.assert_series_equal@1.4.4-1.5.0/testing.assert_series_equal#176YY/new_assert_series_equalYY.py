from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(check_index_type='equiv', check_freq=True, check_exact=False, check_categorical=True, right=b, check_less_precise=False, check_category_order=True, check_names=True, check_datetimelike_compat=False, check_series_type=True, check_dtype=True, left=a, check_index=True)
