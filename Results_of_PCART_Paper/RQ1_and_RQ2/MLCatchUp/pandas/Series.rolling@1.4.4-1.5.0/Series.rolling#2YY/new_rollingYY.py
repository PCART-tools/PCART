import pandas as pd
import numpy as np
df = pd.Series({'B': 0})
df.rolling(window=2).sum()
