from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier(warm_start=False, max_iter=100, monotonic_cst=None, max_depth=None, scoring='loss', learning_rate=0.1, validation_fraction=0.1, min_samples_leaf=20, categorical_features=None, max_leaf_nodes=31, early_stopping='auto', l2_regularization=0.0, n_iter_no_change=10, max_bins=255, interaction_cst=None, class_weight=None)
