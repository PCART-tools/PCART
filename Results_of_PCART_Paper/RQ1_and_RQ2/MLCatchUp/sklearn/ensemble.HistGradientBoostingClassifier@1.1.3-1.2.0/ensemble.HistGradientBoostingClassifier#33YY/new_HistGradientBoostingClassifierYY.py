from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier(categorical_features=None, verbose=0, max_leaf_nodes=31, tol=1e-07, n_iter_no_change=10, l2_regularization=0.0, warm_start=False, early_stopping='auto', scoring='loss', min_samples_leaf=20, monotonic_cst=None, max_bins=255, max_depth=None, validation_fraction=0.1, max_iter=100, learning_rate=0.1, interaction_cst=None, class_weight=None)
