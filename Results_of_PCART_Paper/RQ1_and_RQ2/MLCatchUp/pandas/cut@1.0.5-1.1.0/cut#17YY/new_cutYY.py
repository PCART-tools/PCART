import pandas as pd
import numpy as np
pd.cut(np.array([1, 7, 5, 4, 6, 3]), bins=3, right=True, labels=None, retbins=False)
