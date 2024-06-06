from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(left=a, check_series_type=True, right=b, check_index=True, check_dtype=True, check_index_type='equiv')
