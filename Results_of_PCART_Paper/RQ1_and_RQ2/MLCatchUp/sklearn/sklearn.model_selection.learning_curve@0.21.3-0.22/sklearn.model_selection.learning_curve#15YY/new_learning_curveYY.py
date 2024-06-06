from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import learning_curve
(X, y) = make_classification(n_samples=100, n_features=10, random_state=42)
tree = DecisionTreeClassifier(max_depth=4, random_state=42)
(train_size_abs, train_scores, test_scores) = learning_curve(estimator=tree, X=X, y=y, groups=None, train_sizes=[0.3, 0.6, 0.9], return_times=False)
