import scipy.signal
taps = scipy.signal.firwin(30, cutoff=0.3, fs=None)
