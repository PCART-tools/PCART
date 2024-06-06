import pandas as pd
df = pd.DataFrame({'Animal': ['Falcon', 'Falcon', 'Parrot', 'Parrot'], 'Max Speed': [380.0, 370.0, 24.0, 26.0]})
df.groupby(['Animal'],  0,  None, as_index=True, sort=True, group_keys=False).mean()
