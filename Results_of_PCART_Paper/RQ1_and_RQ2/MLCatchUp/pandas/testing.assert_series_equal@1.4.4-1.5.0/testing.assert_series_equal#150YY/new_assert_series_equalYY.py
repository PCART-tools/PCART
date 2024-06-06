from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(check_less_precise=False, check_index=True, check_index_type='equiv', check_series_type=True, check_exact=False, check_categorical=True, check_dtype=True, left=a, check_category_order=True, right=b, check_datetimelike_compat=False, check_names=True)
