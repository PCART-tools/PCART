from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import learning_curve
(X, y) = make_classification(n_samples=100, n_features=10, random_state=42)
tree = DecisionTreeClassifier(max_depth=4, random_state=42)
(train_size_abs, train_scores, test_scores) = learning_curve(tree, X, y, None, [0.3, 0.6, 0.9], 5, None, False, None, pre_dispatch='all', verbose=0, shuffle=False, random_state=None, return_times=False)
