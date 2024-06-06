from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a,  b, check_names=True, check_dtype=True, check_series_type=True, check_less_precise=False, check_index=True, check_index_type='equiv')
