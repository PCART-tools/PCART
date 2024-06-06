import scipy.signal
taps = scipy.signal.firwin(numtaps=30, cutoff=0.3, width=0.05, fs=None)
