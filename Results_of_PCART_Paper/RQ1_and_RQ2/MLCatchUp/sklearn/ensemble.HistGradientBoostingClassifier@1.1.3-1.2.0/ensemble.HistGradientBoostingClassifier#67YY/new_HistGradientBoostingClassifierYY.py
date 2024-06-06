from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier('log_loss', max_iter=100, max_bins=255, l2_regularization=0.0, max_depth=None, categorical_features=None, scoring='loss', verbose=0, monotonic_cst=None, early_stopping='auto', validation_fraction=0.1, min_samples_leaf=20, tol=1e-07, n_iter_no_change=10, max_leaf_nodes=31, learning_rate=0.1, warm_start=False, interaction_cst=None, class_weight=None)
