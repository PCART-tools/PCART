from PIL import Image, ImageDraw
img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)
draw.arc((50, 50, 250, 250), start=45, end=270, width=0)
