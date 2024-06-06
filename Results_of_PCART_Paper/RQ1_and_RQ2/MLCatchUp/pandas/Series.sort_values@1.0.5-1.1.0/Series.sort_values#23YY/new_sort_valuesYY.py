import pandas as pd
import numpy as np
s = pd.Series([np.nan, 1, 3, 10, 5])
s.sort_values(0,  True,  False,  'quicksort',  'last', ignore_index=False)
