from sklearn.linear_model import LogisticRegression
from sklearn.inspection import permutation_importance
X = [[1, 9, 9], [1, 9, 9], [1, 9, 9], [0, 9, 9], [0, 9, 9], [0, 9, 9]]
y = [1, 1, 1, 0, 0, 0]
clf = LogisticRegression().fit(X, y)
result = permutation_importance(clf, X, n_repeats=10, y=y, scoring=None, random_state=0, n_jobs=None, sample_weight=None)
