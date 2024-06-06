from scipy.stats import qmc
d = 3
centered = False
strength = 1
optimization = None
seed = 42
latin_hypercube = qmc.LatinHypercube(optimization=optimization, centered=centered, d=d, strength=strength)
