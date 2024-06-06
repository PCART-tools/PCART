from matplotlib.path import Path
vertices = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]
codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
path = Path(vertices, codes)
cleaned_path = path.cleaned(None, False, None, stroke_width=1.0, snap=False, simplify=None, curves=False, stroke_width=False, self=None)
print(cleaned_path)
