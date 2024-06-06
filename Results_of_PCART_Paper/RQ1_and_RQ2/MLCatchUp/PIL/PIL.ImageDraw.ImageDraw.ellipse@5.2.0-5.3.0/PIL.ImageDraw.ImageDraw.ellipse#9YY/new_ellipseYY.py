from PIL import Image, ImageDraw
im = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(im)
draw.ellipse(xy=(50, 50, 250, 250), fill='blue', outline='red', width=0)
