import numpy as np
from sklearn.impute import KNNImputer
X = [[1, 2, np.nan], [3, 4, 3], [np.nan, 6, 5], [8, 8, 7]]
imputer = KNNImputer(add_indicator=False, n_neighbors=5, copy=True, weights='uniform', missing_values=np.nan, metric='nan_euclidean', keep_empty_features=False)
