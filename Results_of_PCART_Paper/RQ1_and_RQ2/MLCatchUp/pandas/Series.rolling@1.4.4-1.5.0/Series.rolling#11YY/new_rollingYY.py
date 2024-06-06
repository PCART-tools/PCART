import pandas as pd
import numpy as np
df = pd.Series({'B': 0})
df.rolling(2,  None,  False, win_type=None).sum()
