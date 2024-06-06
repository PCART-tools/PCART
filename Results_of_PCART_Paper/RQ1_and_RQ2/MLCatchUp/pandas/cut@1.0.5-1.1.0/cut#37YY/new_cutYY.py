import pandas as pd
import numpy as np
pd.cut(np.array([1, 7, 5, 4, 6, 3]),  3,  True,  None,  False, precision=3, include_lowest=False, duplicates='raise')
