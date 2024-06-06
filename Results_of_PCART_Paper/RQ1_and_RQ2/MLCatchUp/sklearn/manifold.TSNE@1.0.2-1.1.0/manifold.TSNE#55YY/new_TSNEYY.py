import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(2, angle=0.5, early_exaggeration=12.0, random_state=None, init='warn', min_grad_norm=1e-07, perplexity=30.0, n_iter=1000, learning_rate='warn', verbose=0, n_jobs=None, method='barnes_hut', metric='euclidean', n_iter_without_progress=300).fit_transform(X, metric_params=None)
