from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a,  b,  True,  'equiv',  True,  False,  True,  False,  False,  True,  True,  True, rtol=1e-05, check_index=True, atol=1e-08, check_flags=True, obj='Series')
