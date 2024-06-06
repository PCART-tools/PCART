import pandas as pd
import numpy as np
df = pd.Series({'B': 0})
df.ewm(com=0.5, span=None, halflife=None, alpha=None, min_periods=0, adjust=True).mean()
