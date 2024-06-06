import pandas as pd
ser = pd.Series([390.0, 350.0, 30.0, 20.0], index=['Falcon', 'Falcon', 'Parrot', 'Parrot'], name='Max Speed')
ser.groupby(by=['a', 'b', 'a', 'b'], axis=0).mean()
