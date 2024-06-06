import numpy as np
from scipy.signal import welch
x = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
fs = 10.0
(frequencies, power_density) = welch(x, fs, window='hann', nperseg=None, noverlap=None, nfft=None, detrend='constant', return_onesided=True, average='mean')
