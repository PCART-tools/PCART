import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(2, metric='euclidean', perplexity=30.0, early_exaggeration=12.0, learning_rate='warn', n_iter=1000, min_grad_norm=1e-07, n_iter_without_progress=300).fit_transform(X, metric_params=None)
