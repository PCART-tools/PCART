import scipy.signal
(w0, Q) = (0.5, 2.0)
response = scipy.signal.iirpeak(w0, Q=Q, fs=2.0)
