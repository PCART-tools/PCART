from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier(early_stopping='auto', max_depth=None, min_samples_leaf=20, monotonic_cst=None, loss='log_loss', l2_regularization=0.0, max_iter=100, learning_rate=0.1, warm_start=False, max_bins=255, categorical_features=None, max_leaf_nodes=31, interaction_cst=None, class_weight=None)
