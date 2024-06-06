from sklearn.svm import SVC
from sklearn.ensemble import BaggingClassifier
from sklearn.datasets import make_classification
(X, y) = make_classification(n_samples=100, n_features=4, n_informative=2, n_redundant=0, random_state=0, shuffle=False)
clf = BaggingClassifier(oob_score=False, n_jobs=None, verbose=0, max_samples=1.0, max_features=1.0, bootstrap=True, random_state=None, n_estimators=10, warm_start=False, bootstrap_features=False, base_estimator=SVC()).fit(y, base_estimator=X, estimator=None)
