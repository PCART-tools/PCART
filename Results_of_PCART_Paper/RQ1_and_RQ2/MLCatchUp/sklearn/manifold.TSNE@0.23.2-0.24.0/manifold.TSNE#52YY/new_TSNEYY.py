import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(2, learning_rate=200.0, init='random', n_iter=1000, n_iter_without_progress=300, method='barnes_hut', early_exaggeration=12.0, metric='euclidean', n_jobs=None, verbose=0, random_state=None, min_grad_norm=1e-07, angle=0.5, perplexity=30.0).fit_transform(X, square_distances='legacy')
