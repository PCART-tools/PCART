import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(2, angle=0.5, metric='euclidean', n_iter_without_progress=300, verbose=0, init='random', learning_rate=200.0, random_state=None, method='barnes_hut', n_iter=1000, min_grad_norm=1e-07, early_exaggeration=12.0, perplexity=30.0).fit_transform(X, square_distances='legacy')
