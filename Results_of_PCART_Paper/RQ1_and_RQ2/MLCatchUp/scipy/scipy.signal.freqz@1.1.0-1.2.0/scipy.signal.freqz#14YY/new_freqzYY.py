from scipy.signal import freqz
b = [1.0, -2.0, 1.0]
a = [1.0, -0.5, 0.25]
worN = 512
whole = False
plot = None
freqz(b=b, a=a, worN=worN, whole=whole, fs=6.283185307179586)
