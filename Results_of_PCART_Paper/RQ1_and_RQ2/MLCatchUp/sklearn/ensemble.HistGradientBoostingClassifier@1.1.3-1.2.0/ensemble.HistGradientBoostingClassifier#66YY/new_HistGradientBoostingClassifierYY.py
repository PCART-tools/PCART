from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier('log_loss', categorical_features=None, max_depth=None, learning_rate=0.1, max_bins=255, n_iter_no_change=10, scoring='loss', monotonic_cst=None, max_leaf_nodes=31, max_iter=100, validation_fraction=0.1, tol=1e-07, warm_start=False, l2_regularization=0.0, early_stopping='auto', min_samples_leaf=20, interaction_cst=None, class_weight=None)
