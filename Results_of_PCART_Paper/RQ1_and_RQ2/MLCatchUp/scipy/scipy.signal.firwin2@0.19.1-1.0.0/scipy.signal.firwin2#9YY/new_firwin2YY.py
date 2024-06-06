import scipy.signal
coeff = scipy.signal.firwin2(64, [0.0, 0.5], [1.0, 0.0], 512, 'hamming', 0.5, antisymmetric=False, fs=None)
