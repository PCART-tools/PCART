import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(imputation_order='ascending', min_value=(- 0), skip_complete=False, sample_posterior=False, max_value=0, initial_strategy='mean', missing_values=0, verbose=0, n_nearest_features=None, random_state=None, max_iter=10, estimator=None, tol=0.001, fill_value=None)
