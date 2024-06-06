import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(n_iter_without_progress=300, min_grad_norm=1e-07, perplexity=30.0, early_exaggeration=12.0, verbose=0, metric='euclidean', init='random', learning_rate=200.0, n_iter=1000).fit_transform(X, square_distances='legacy')
