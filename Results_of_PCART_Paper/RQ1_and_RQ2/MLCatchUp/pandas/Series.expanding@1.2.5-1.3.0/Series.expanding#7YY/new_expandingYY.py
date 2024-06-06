import pandas as pd
import numpy as np
df = pd.Series({'B': 0})
df.expanding(1,  False,  0).sum()
