from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier(max_bins=255, l2_regularization=0.0, learning_rate=0.1, max_leaf_nodes=31, min_samples_leaf=20, monotonic_cst=None, scoring='loss', max_iter=100, categorical_features=None, warm_start=False, max_depth=None, early_stopping='auto', validation_fraction=0.1, interaction_cst=None, class_weight=None)
