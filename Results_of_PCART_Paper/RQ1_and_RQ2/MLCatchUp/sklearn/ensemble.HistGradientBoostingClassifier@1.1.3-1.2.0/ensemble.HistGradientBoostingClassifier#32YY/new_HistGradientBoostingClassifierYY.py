from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier(warm_start=False, tol=1e-07, max_depth=None, l2_regularization=0.0, validation_fraction=0.1, min_samples_leaf=20, n_iter_no_change=10, max_leaf_nodes=31, max_bins=255, categorical_features=None, scoring='loss', learning_rate=0.1, early_stopping='auto', max_iter=100, monotonic_cst=None, interaction_cst=None, class_weight=None)
