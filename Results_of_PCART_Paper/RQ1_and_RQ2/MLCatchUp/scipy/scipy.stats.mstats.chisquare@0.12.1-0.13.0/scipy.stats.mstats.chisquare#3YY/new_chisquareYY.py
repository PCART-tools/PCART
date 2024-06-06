import numpy as np
import scipy.stats as stats
f_obs = [16, 18, 16, 14, 12, 12]
f_exp = [16, 16, 16, 16, 16, 8]
f_exp = np.array(f_exp)
result = stats.mstats.chisquare(f_obs, f_exp, ddof=0, axis=0)
