import pandas as pd
import numpy as np
s = pd.Series([1, 2, 3, 4], name='foo', index=pd.Index(['a', 'b', 'c', 'd'], name='idx'))
s.reset_index(level=None)
