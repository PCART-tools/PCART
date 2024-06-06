import numpy as np
from sklearn.impute import KNNImputer
X = [[1, 2, np.nan], [3, 4, 3], [np.nan, 6, 5], [8, 8, 7]]
imputer = KNNImputer(missing_values=np.nan, n_neighbors=5, metric='nan_euclidean', weights='uniform', keep_empty_features=False)
