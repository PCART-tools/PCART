from sklearn.datasets import make_friedman1
from sklearn.feature_selection import RFECV
from sklearn.svm import SVR
(X, y) = make_friedman1(n_samples=50, n_features=10, random_state=0)
estimator = SVR(kernel='linear')
selector = RFECV(estimator,  5,  None, scoring=None)
