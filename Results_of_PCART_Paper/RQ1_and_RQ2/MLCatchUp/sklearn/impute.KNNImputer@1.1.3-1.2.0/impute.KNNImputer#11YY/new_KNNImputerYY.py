import numpy as np
from sklearn.impute import KNNImputer
X = [[1, 2, np.nan], [3, 4, 3], [np.nan, 6, 5], [8, 8, 7]]
imputer = KNNImputer(metric='nan_euclidean', missing_values=np.nan, weights='uniform', copy=True, n_neighbors=5, keep_empty_features=False)
