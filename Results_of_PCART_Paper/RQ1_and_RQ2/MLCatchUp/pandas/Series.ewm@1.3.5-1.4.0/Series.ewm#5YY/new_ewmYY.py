import pandas as pd
import numpy as np
df = pd.Series({'B': 0})
df.ewm(com=0.5, span=None).mean()
