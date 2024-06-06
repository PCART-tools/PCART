import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(sample_posterior=False, n_nearest_features=None, max_iter=10, missing_values=0, estimator=None, tol=0.001, fill_value=None)
