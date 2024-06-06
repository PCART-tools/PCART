import pandas as pd
import numpy as np
df = pd.Series({'B': 0})
df.rolling(2,  None, center=False, win_type=None, on=None, axis=0).sum()
