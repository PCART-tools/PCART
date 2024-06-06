import pandas as pd
df = pd.DataFrame(data={'animal_1': ['elk', 'pig'], 'animal_2': ['dog', 'quetzal']})
print(df.to_markdown(None,  None))
