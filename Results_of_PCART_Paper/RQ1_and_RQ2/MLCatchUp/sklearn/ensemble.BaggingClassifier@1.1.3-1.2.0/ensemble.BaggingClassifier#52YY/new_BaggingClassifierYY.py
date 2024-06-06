from sklearn.svm import SVC
from sklearn.ensemble import BaggingClassifier
from sklearn.datasets import make_classification
(X, y) = make_classification(n_samples=100, n_features=4, n_informative=2, n_redundant=0, random_state=0, shuffle=False)
clf = BaggingClassifier(bootstrap_features=False, bootstrap=True, max_features=1.0, warm_start=False, oob_score=False, base_estimator=SVC(), max_samples=1.0, n_jobs=None).fit(y, base_estimator=X, estimator=None)
