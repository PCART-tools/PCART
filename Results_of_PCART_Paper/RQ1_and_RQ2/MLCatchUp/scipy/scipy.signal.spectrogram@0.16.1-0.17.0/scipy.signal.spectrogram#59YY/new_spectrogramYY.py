import numpy as np
from scipy.signal import spectrogram
x = np.random.randn(1000)
fs = 8000
nperseg = 256
noverlap = int(0.5 * nperseg)
nfft = nperseg
detrend = 'constant'
return_onesided = True
scaling = 'density'
axis = -1
(frequencies, times, Sxx) = spectrogram(x, fs, 'hann', nperseg, noverlap, nfft, detrend=detrend, return_onesided=return_onesided, scaling=scaling, axis=axis, mode='psd')
