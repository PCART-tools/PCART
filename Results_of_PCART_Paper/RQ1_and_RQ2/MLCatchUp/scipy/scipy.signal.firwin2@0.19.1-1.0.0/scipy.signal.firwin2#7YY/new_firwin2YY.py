import scipy.signal
coeff = scipy.signal.firwin2(numtaps=64, freq=[0.0, 0.5], gain=[1.0, 0.0], nfreqs=512, window='hamming', nyq=0.5, fs=None)
