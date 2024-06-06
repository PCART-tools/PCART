from PIL import ImageFont
font = ImageFont.load_default()
text = 'Hello, Pillow!'
mask = font.getmask(text, '1', None, None, None, stroke_width=0, anchor=None, ink=0, start=None)
