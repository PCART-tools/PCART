from scipy.stats import zmap
scores = [45, 50, 55, 60]
compare = [50, 50, 50, 50]
axis = 0
ddof = 0
result = zmap(scores, compare, axis, ddof=ddof, nan_policy='propagate')
