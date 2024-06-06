from PIL import ImageFont
font = ImageFont.load_default()
text = 'Hello, Pillow!'
mask = font.getmask(text, '1', None, None, language=None, stroke_width=0, anchor=None, start=None)
