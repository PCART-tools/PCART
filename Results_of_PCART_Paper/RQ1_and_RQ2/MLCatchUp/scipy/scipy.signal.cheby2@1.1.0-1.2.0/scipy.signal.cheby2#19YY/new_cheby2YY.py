from scipy import signal
N = 4
rs = 40
Wn = 0.4
btype = 'low'
analog = False
output = 'ba'
signal.cheby2(N, rs, Wn, btype=btype, analog=analog, output=output, fs=None)
