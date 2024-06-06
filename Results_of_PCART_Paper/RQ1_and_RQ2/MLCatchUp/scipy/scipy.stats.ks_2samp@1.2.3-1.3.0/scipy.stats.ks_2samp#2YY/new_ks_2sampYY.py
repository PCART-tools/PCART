import scipy.stats
data1 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 1.364, 0.559, -0.742]
data2 = [-0.629, 0.664, -0.959, 0.789, -0.418, -0.951, 0.085, -0.623, 0.492]
result = scipy.stats.ks_2samp(data1, data2=data2, alternative='two-sided', mode='auto')
