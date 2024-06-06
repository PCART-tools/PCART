import pandas as pd
index = pd.Index(['A', 'B', 'C', 'D', 'E'])
start = 'B'
end = 'D'
step = None
start_bound = index.get_slice_bound(label=start, side='left', kind=None)
