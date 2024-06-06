import scipy.signal as signal
b = [0.25, 0, -0.25]
a = [1, -0.5]
worN = 256
whole = False
fs = 2 * 3.141592653589793
signal.freqz(b=b, a=a, worN=worN, whole=whole, plot=None, fs=fs, include_nyquist=False)
