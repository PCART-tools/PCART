import pandas as pd
data = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1], 'C': [2, 3, 2, 3, 2]}
df = pd.DataFrame(data)
cov_matrix = df.cov(min_periods=None)
print(cov_matrix)
