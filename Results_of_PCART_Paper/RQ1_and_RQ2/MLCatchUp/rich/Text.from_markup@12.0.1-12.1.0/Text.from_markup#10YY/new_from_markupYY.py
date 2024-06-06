from rich.text import Text
from rich.style import Style
from rich.console import EmojiVariant
text_obj = Text.from_markup('Hello', emoji=True, overflow='fold', justify='center', emoji_variant=None, style='red', end='\n')
