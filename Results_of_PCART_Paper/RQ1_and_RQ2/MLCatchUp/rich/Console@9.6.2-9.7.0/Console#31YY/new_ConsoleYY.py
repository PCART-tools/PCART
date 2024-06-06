from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(force_jupyter=None, force_terminal=None, stderr=False, file=sys.stdout, color_system='auto', soft_wrap=False, theme=Theme(), no_color=None)
