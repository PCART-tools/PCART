import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(2, n_iter_without_progress=300, verbose=0, init='warn', learning_rate='warn', early_exaggeration=12.0, n_iter=1000, perplexity=30.0, method='barnes_hut', metric='euclidean', random_state=None, min_grad_norm=1e-07).fit_transform(X, metric_params=None)
