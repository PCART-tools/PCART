import pandas as pd
index = pd.date_range('1/1/2000', periods=9, freq='T')
DataFrame = pd.DataFrame(range(9), index=index)
DataFrame.resample(rule='3T', axis=0, closed=None, label=None, convention='start', kind=None).sum()
