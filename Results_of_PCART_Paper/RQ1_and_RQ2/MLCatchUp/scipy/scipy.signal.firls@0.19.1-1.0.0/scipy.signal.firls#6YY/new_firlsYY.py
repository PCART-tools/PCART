import scipy.signal
numtaps = 65
bands = [0, 0.1, 0.2, 0.5]
desired = [1, 0, 1, 1]
weight = [1, 100]
taps = scipy.signal.firls(numtaps, bands, desired, weight=weight, fs=None)
