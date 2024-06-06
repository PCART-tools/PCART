import pandas as pd
df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'}, 'B': {0: 1, 1: 3, 2: 5}, 'C': {0: 2, 1: 4, 2: 6}})
pd.melt(frame=df, id_vars=['A'], value_vars=['B'], var_name=None, value_name='value', col_level=None)
