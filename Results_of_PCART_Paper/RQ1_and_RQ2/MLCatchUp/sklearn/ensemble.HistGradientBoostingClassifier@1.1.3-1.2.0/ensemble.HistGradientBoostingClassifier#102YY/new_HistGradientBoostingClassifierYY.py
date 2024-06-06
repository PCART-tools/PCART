from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier(max_depth=None, max_leaf_nodes=31, validation_fraction=0.1, scoring='loss', n_iter_no_change=10, learning_rate=0.1, tol=1e-07, early_stopping='auto', max_bins=255, min_samples_leaf=20, max_iter=100, random_state=None, l2_regularization=0.0, verbose=0, monotonic_cst=None, categorical_features=None, loss='log_loss', warm_start=False, interaction_cst=None, class_weight=None)
