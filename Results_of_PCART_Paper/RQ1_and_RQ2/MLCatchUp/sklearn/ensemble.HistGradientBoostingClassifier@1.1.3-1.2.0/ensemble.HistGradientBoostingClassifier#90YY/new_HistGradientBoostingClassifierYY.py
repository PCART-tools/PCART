from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier(learning_rate=0.1, loss='log_loss', min_samples_leaf=20, max_leaf_nodes=31, max_depth=None, max_iter=100, interaction_cst=None, class_weight=None)
