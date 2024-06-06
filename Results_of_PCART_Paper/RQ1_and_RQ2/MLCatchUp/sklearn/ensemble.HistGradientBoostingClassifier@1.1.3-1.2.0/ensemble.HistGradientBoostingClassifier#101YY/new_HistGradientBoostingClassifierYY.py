from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier(monotonic_cst=None, max_iter=100, verbose=0, min_samples_leaf=20, max_leaf_nodes=31, warm_start=False, learning_rate=0.1, validation_fraction=0.1, early_stopping='auto', l2_regularization=0.0, max_bins=255, n_iter_no_change=10, loss='log_loss', categorical_features=None, max_depth=None, scoring='loss', tol=1e-07, interaction_cst=None, class_weight=None)
