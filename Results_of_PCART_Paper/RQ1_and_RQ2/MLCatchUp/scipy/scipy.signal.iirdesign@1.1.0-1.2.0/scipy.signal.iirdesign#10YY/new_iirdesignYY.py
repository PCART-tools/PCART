from scipy.signal import iirdesign
wp = 0.1
ws = 0.15
gpass = 1
gstop = 40
(b, a) = iirdesign(wp, ws=ws, gpass=gpass, gstop=gstop, analog=False, fs=None)
