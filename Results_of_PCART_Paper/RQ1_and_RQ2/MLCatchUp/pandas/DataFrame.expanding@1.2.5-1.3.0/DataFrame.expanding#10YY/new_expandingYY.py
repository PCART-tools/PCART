import pandas as pd
import numpy as np
df = pd.DataFrame({'B': [0, 1, 2, np.nan, 4]})
df.expanding(min_periods=2, center=None, axis=0).sum()
