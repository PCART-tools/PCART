import numpy as np
from sklearn.impute import SimpleImputer
imp_mean = SimpleImputer(np.nan, 'mean', None, 0, copy=True, add_indicator=False)
