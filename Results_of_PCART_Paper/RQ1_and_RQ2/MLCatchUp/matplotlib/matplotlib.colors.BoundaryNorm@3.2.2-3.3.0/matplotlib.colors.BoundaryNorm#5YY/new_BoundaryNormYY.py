import matplotlib.colors as mcolors
boundaries = [1, 2, 3, 4, 5]
ncolors = 6
clip = False
norm = mcolors.BoundaryNorm(boundaries, ncolors, clip=clip, extend='neither')
