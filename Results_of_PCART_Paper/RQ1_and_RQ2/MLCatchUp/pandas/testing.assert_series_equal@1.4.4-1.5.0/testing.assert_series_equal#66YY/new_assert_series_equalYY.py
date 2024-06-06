from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(check_less_precise=False, check_dtype=True, right=b, check_names=True, check_index=True, left=a, check_index_type='equiv', check_series_type=True)
