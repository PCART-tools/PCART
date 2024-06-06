import numpy as np
from sklearn.impute import SimpleImputer
imp_mean = SimpleImputer(np.nan, 'mean', None, 0, True, add_indicator=False)
