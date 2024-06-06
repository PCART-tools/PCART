from matplotlib.path import Path
vertices = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]
codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
path = Path(vertices, codes)
cleaned_path = path.cleaned(None, remove_nans=False, clip=None, quantize=None, simplify=False)
print(cleaned_path)
