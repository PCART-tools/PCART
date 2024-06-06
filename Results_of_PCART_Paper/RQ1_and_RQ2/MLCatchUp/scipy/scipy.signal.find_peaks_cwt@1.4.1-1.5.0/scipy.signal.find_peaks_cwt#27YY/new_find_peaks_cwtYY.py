from scipy.signal import find_peaks_cwt
vector = [1, 2, 3, 2, 1, 3, 5, 4, 3, 2, 1]
widths = [1, 2, 3]
min_length = 2
peaks = find_peaks_cwt(vector, widths, None, None, None, min_length, min_snr=1, window_size=None)
print(peaks)
