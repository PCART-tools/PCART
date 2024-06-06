from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier(max_bins=255, max_leaf_nodes=31, max_iter=100, warm_start=False, monotonic_cst=None, loss='log_loss', l2_regularization=0.0, scoring='loss', categorical_features=None, learning_rate=0.1, min_samples_leaf=20, early_stopping='auto', max_depth=None, interaction_cst=None, class_weight=None)
