from PIL import Image, ImageDraw
image = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(image)
draw.line((50, 50, 250, 250), joint=None)
