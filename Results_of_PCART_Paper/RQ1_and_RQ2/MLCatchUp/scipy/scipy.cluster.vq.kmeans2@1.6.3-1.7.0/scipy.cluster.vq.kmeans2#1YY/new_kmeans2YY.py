from scipy.cluster.vq import kmeans2
data = [[1.2, 2.3], [2.4, 3.5], [3.6, 4.7], [4.8, 5.9], [6.0, 7.1]]
k = 2
iter = 5
thresh = 1e-06
minit = 'points'
missing = 'warn'
check_finite = False
kmeans2(data, k, iter, thresh, minit, seed=None)
