from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(stderr=False, soft_wrap=False, theme=Theme(), force_terminal=None, width=80, force_jupyter=None, file=sys.stdout, color_system='auto', no_color=None)
