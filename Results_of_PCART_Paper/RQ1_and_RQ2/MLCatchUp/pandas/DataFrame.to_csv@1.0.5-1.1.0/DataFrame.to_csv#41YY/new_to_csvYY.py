import pandas as pd
df = pd.DataFrame({'name': ['Raphael', 'Donatello'], 'mask': ['red', 'purple'], 'weapon': ['sai', 'bo staff']})
df.to_csv(None,  ',',  '',  None, columns=None, header=True, index=False, index_label=None)
