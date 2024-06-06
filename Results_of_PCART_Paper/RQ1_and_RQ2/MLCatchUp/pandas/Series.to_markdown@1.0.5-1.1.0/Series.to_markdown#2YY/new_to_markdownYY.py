import pandas as pd
s = pd.Series(['elk', 'pig', 'dog', 'quetzal'], name='animal')
print(s.to_markdown(None))
