import pandas as pd
import numpy as np
df = pd.DataFrame({'B': [0, 1, 2, np.nan, 4]})
df.ewm(com=0.5, span=None, halflife=None, alpha=None, min_periods=0).mean()
