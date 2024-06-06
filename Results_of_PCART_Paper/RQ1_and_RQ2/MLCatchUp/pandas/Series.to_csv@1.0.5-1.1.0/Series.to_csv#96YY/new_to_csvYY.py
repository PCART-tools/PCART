import pandas as pd
df = pd.Series({'name': ['Raphael', 'Donatello'], 'mask': ['red', 'purple'], 'weapon': ['sai', 'bo staff']})
df.to_csv(None,  ',',  '',  None,  None,  True,  False,  None,  'w', encoding=None, compression='infer', quoting=None, quotechar='"',line_terminator=None,chunksize=None,date_format=None,doublequote=True,escapechar=None,decimal='.')
