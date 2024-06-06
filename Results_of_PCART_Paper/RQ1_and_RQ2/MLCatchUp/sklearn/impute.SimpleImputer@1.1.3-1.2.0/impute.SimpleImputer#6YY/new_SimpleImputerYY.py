import numpy as np
from sklearn.impute import SimpleImputer
imp_mean = SimpleImputer(copy=True, keep_empty_features=False)
