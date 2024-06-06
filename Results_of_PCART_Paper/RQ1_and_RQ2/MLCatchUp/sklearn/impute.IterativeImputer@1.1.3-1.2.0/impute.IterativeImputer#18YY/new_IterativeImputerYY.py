import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(missing_values=0, sample_posterior=False, n_nearest_features=None, max_iter=10, tol=0.001, keep_empty_features=False)
