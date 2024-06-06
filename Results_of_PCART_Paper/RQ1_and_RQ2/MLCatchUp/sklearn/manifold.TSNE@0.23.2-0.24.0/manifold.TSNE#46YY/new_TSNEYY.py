import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(2, learning_rate=200.0, metric='euclidean', early_exaggeration=12.0, min_grad_norm=1e-07, n_iter_without_progress=300, perplexity=30.0, n_iter=1000).fit_transform(X, square_distances='legacy')
