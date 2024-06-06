import pandas as pd
s1 = pd.Series([0.90010907, 0.13484424, 0.62036035])
s2 = pd.Series([0.12528585, 0.26962463, 0.51111198])
s1.cov(s2,  None)
