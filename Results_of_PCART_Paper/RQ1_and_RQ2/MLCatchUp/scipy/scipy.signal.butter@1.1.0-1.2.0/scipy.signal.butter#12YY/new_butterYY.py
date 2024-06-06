from scipy.signal import butter
N = 4
Wn = 0.2
btype = 'low'
analog = False
output = 'ba'
butter(N=N, Wn=Wn, btype=btype, analog=analog, fs=None)
