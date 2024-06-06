import pandas as pd
index = pd.date_range('1/1/2000', periods=9, freq='T')
series = pd.Series(range(9), index=index)
series.resample('3T',  0,  None,  None,  'start',  None,  None, base=None).sum()
