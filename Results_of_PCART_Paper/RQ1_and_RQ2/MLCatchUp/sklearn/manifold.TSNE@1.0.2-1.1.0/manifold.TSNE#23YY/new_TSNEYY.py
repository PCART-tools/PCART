import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(min_grad_norm=1e-07, early_exaggeration=12.0, perplexity=30.0, n_iter=1000, verbose=0, learning_rate='warn', init='warn', n_iter_without_progress=300, metric='euclidean').fit_transform(X, metric_params=None)
