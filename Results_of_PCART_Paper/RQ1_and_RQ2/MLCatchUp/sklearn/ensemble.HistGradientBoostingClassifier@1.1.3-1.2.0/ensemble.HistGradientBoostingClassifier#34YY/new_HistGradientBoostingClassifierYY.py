from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier(max_leaf_nodes=31, max_iter=100, scoring='loss', learning_rate=0.1, verbose=0, categorical_features=None, l2_regularization=0.0, monotonic_cst=None, random_state=None, min_samples_leaf=20, tol=1e-07, n_iter_no_change=10, early_stopping='auto', max_bins=255, max_depth=None, validation_fraction=0.1, warm_start=False, interaction_cst=None, class_weight=None)
