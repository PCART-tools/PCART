import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(sample_posterior=False, estimator=None, missing_values=0, keep_empty_features=False)
