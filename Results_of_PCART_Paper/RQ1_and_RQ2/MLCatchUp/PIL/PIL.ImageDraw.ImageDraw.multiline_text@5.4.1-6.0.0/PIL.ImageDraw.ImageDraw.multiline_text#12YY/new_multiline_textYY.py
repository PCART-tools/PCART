from PIL import Image, ImageDraw, ImageFont
image = Image.new('RGB', (300, 150), 'white')
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
xy = (10, 10)
text = 'Hello, Pillow!'
fill = 'black'
anchor = 'lt'
spacing = 4
align = 'left'
direction = None
features = None
draw.multiline_text(xy=xy, text=text, fill=fill, font=font, language=None)
