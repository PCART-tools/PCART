import pandas as pd
import numpy as np
df = pd.Series({'B': 0})
df.rolling(2, min_periods=None, center=False, win_type=None, on=None).sum()
