import pandas as pd
index = pd.date_range('1/1/2000', periods=9, freq='T')
series = pd.Series(range(9), index=index)
series.resample('3T',  0,  None,  None, convention='start', kind=None, loffset=None, base=None, on=None, level=None, origin='start_day', offset=None, group_keys=False).sum()
