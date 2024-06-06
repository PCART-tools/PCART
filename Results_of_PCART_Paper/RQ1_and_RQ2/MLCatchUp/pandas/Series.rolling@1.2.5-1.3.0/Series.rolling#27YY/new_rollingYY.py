import pandas as pd
import numpy as np
df = pd.Series({'B': 1})
df.rolling(window=2, min_periods=None, center=False, win_type='triang', on=None, axis=0).sum()
