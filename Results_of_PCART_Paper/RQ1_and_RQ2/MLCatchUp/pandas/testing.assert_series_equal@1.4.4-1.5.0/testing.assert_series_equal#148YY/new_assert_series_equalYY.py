from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a, check_index_type='equiv', check_dtype=True, check_category_order=True, check_exact=False, check_categorical=True, right=b, check_datetimelike_compat=False, check_less_precise=False, check_names=True, check_series_type=True, check_index=True)
