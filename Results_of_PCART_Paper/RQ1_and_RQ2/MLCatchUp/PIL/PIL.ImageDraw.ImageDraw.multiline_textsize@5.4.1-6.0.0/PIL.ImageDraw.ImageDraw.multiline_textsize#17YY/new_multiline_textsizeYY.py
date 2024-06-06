from PIL import Image, ImageDraw, ImageFont

def example_usage():
    image = Image.new('RGB', (100, 100), 'white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    text = 'Hello\nWorld'
    spacing = 4
    size = draw.multiline_textsize(text, font, spacing, direction=None, features=None, language=None)
if __name__ == '__main__':
    example_usage()
