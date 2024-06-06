from scipy.stats import qmc
d = 3
scramble = True
seed = 123
sobol = qmc.Sobol(d, scramble=scramble, seed=seed)
