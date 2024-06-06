import scipy.signal
taps = scipy.signal.firwin(30, 0.3, width=0.05, window='hamming', fs=None)
