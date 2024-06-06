from scipy.stats import entropy
pk = [0.4, 0.6]
qk = [0.5, 0.5]
base = 2.0
result = entropy(pk, axis=0)
