from scipy.signal import butter
N = 4
Wn = 0.2
btype = 'low'
analog = False
output = 'ba'
butter(N, Wn=Wn, fs=None)
