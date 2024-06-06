from sklearn.datasets import make_friedman1
from sklearn.feature_selection import RFECV
from sklearn.svm import SVR
(X, y) = make_friedman1(n_samples=50, n_features=10, random_state=0)
estimator = SVR(kernel='linear')
selector = RFECV(estimator, cv=5, step=1, verbose=0, scoring=None, min_features_to_select=1, n_jobs=None, importance_getter='auto')
