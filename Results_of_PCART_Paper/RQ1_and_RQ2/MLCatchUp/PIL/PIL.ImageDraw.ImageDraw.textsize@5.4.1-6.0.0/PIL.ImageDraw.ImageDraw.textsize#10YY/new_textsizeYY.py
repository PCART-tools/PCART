from PIL import Image, ImageDraw, ImageFont
image = Image.new('RGB', (100, 100), 'white')
font = ImageFont.load_default()
draw = ImageDraw.Draw(image)
text = 'Hello, Pillow!'
size = draw.textsize(text, font, 4, None, language=None)
