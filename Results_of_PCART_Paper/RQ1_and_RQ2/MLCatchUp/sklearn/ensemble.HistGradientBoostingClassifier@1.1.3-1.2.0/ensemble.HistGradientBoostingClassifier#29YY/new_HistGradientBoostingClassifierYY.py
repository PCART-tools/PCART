from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier(max_depth=None, max_bins=255, learning_rate=0.1, categorical_features=None, scoring='loss', monotonic_cst=None, max_leaf_nodes=31, max_iter=100, early_stopping='auto', warm_start=False, min_samples_leaf=20, l2_regularization=0.0, interaction_cst=None, class_weight=None)
