from PIL import Image, ImageDraw
image = Image.new('RGB', (200, 200), 'white')
draw = ImageDraw.Draw(image)
draw.rectangle((50, 50, 150, 150), None, width=0)
