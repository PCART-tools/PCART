import numpy as np
from scipy import stats
f_obs = [16, 18, 16, 14, 12, 12]
f_exp = [16, 16, 16, 16, 16, 8]
f_exp = np.array(f_exp)
result = stats.chisquare(f_obs=f_obs, f_exp=f_exp, ddof=3, axis=0)
