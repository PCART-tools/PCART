import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(early_exaggeration=12.0, n_iter_without_progress=300, learning_rate='warn', metric='euclidean', n_iter=1000, min_grad_norm=1e-07, perplexity=30.0).fit_transform(X, metric_params=None)
