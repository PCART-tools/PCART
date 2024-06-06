import pandas as pd
int_values = [1, 2, 3, 4, 5]
text_values = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
float_values = [0.0, 0.25, 0.5, 0.75, 1.0]
df = pd.DataFrame({'int_col': int_values, 'text_col': text_values, 'float_col': float_values})
df.info(True,  None)
