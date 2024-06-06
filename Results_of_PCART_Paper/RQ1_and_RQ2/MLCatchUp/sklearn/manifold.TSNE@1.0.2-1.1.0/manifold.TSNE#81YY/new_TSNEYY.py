import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(verbose=0, n_iter=1000, method='barnes_hut', n_iter_without_progress=300, early_exaggeration=12.0, learning_rate='warn', metric='euclidean', random_state=None, init='warn', perplexity=30.0, n_components=2, min_grad_norm=1e-07).fit_transform(X, metric_params=None)
