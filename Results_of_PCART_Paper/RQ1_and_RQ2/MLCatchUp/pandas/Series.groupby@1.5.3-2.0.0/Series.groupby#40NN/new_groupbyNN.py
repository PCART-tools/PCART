import pandas as pd
ser = pd.Series([390.0, 350.0, 30.0, 20.0], index=['Falcon', 'Falcon', 'Parrot', 'Parrot'], name='Max Speed')
ser.groupby(['a', 'b', 'a', 'b'],  0,  None,  True, sort=True, group_keys=False, squeeze=False, observed=False).mean()
