import pandas as pd
import numpy as np
df = pd.Series({'B': 1})
df.rolling(2,  None, center=False, win_type='triang', on=None).sum()
