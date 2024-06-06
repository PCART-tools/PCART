import matplotlib.colors as mcolors
linthresh = 0.1
linscale = 1.0
vmin = None
vmax = None
clip = False
norm = mcolors.SymLogNorm(linthresh, linscale, vmin=vmin, vmax=vmax, clip=clip, base=None)
