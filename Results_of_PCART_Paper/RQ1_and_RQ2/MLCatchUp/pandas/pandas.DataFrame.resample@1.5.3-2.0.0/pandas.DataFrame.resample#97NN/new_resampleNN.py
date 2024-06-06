import pandas as pd
index = pd.date_range('1/1/2000', periods=9, freq='T')
DataFrame = pd.DataFrame(range(9), index=index)
DataFrame.resample('3T',  0,  None,  None,  'start',  None,  None, base=None, on=None, level=None, origin='start_day', offset=None, group_keys=False).sum()
