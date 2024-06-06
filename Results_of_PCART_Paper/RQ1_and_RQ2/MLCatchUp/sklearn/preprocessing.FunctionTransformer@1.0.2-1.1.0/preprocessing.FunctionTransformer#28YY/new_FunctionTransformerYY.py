import numpy as np
from sklearn.preprocessing import FunctionTransformer
transformer = FunctionTransformer(validate=False, check_inverse=True, accept_sparse=False, func=None, feature_names_out=None)
