import pandas as pd
d = {'price': [10, 11, 9, 13, 14, 18, 17, 19], 'volume': [50, 60, 40, 100, 50, 100, 40, 50]}
df = pd.DataFrame(d)
df['week_starting'] = pd.date_range('01/01/2018', periods=8, freq='W')
df.resample('M',  0,  None,  None,  'start',  None,  None, base=None, on='week_starting').mean()
