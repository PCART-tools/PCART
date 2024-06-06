from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier(warm_start=False, l2_regularization=0.0, max_depth=None, early_stopping='auto', max_bins=255, learning_rate=0.1, monotonic_cst=None, categorical_features=None, min_samples_leaf=20, max_iter=100, max_leaf_nodes=31, interaction_cst=None, class_weight=None)
