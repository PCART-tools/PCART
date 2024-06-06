from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a,  b,  True,  'equiv',  True,  False,  True,  False, check_index=True, rtol=1e-05, check_category_order=True, obj='Series', atol=1e-08, check_categorical=True, check_flags=True, check_datetimelike_compat=False, check_freq=True)
