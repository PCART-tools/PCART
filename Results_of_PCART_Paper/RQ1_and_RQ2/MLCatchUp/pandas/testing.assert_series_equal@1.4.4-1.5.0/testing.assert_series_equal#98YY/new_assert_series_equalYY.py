from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a,  b,  True, check_exact=False, check_datetimelike_compat=False, check_names=True, check_series_type=True, check_less_precise=False, check_index_type='equiv', check_index=True)
