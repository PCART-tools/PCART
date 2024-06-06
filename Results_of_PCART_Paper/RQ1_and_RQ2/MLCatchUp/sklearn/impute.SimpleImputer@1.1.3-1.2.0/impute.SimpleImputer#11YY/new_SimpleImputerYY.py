import numpy as np
from sklearn.impute import SimpleImputer
imp_mean = SimpleImputer(strategy='mean', verbose='deprecated', copy=True, missing_values=np.nan, fill_value=None, keep_empty_features=False)
