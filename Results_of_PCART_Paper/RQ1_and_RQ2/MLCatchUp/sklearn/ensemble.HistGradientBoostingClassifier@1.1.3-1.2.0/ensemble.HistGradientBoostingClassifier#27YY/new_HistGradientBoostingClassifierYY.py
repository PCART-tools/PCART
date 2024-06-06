from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier(min_samples_leaf=20, max_depth=None, learning_rate=0.1, categorical_features=None, l2_regularization=0.0, max_bins=255, monotonic_cst=None, warm_start=False, max_leaf_nodes=31, max_iter=100, interaction_cst=None, class_weight=None)
