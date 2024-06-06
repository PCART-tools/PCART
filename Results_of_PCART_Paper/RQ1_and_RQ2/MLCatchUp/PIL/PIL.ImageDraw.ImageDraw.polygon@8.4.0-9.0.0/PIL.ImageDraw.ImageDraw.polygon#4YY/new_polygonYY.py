from PIL import Image, ImageDraw
im = Image.new('RGB', (200, 200), 'white')
draw = ImageDraw.Draw(im)
xy2 = [(20, 20), (180, 20), (100, 150)]
fill_color = 'red'
outline_color = 'blue'
draw.polygon(xy2, fill=fill_color, width=1)
