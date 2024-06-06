import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(None, initial_strategy='mean', sample_posterior=False, n_nearest_features=None, missing_values=0, tol=0.001, imputation_order='ascending', max_iter=10, fill_value=None)
