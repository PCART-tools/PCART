import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(init='random', n_jobs=None, verbose=0, learning_rate=200.0, angle=0.5, n_iter_without_progress=300, method='barnes_hut', random_state=None, min_grad_norm=1e-07, perplexity=30.0, n_iter=1000, early_exaggeration=12.0, metric='euclidean').fit_transform(X, square_distances='legacy')
