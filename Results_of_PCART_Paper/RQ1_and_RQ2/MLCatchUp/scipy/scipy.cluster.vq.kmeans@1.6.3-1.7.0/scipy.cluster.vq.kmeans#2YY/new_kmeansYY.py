from scipy.cluster.vq import kmeans
obs = [[1.2, 2.3], [0.4, 4.5], [2.4, 2.5], [2.0, 3.7], [1.5, 0.5]]
k_or_guess = 3
iter = 30
thresh = 1e-06
kmeans(obs, k_or_guess=k_or_guess, seed=None)
