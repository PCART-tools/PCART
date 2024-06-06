from scipy.signal import cheby1
N = 4
rp = 1
Wn = 0.4
btype = 'low'
analog = False
output = 'ba'
cheby1(N, rp, Wn, btype, analog, output=output, fs=None)
