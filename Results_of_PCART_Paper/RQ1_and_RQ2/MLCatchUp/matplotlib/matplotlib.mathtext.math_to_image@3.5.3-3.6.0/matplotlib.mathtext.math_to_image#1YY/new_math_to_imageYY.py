import matplotlib.mathtext as mathtext
s = '$\\frac{1}{2} \\times \\sqrt{4}$'
filename_or_obj = 'output.png'
dpi = 100
format = 'png'
mathtext.math_to_image(s, filename_or_obj, color=None)
