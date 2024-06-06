import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(n_iter_without_progress=300, min_grad_norm=1e-07, n_iter=1000, metric='euclidean', perplexity=30.0, early_exaggeration=12.0, init='warn', learning_rate='warn').fit_transform(X, metric_params=None)
