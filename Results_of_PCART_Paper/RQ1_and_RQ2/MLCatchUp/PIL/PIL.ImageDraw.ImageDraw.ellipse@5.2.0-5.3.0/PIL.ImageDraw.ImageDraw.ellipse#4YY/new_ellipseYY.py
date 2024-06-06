from PIL import Image, ImageDraw
im = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(im)
draw.ellipse((50, 50, 250, 250), fill='blue', width=0)
