import pandas as pd
import numpy as np
df = pd.DataFrame({'B': [0, 1, 2, np.nan, 4]})
df.ewm(0.5,  None,  None,  None,  0,  True,  False,  0,  None).mean()
