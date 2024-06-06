import pandas as pd
import numpy as np
df = pd.Series({'B': 0})
df.expanding(1, center=False, axis=0).sum()
