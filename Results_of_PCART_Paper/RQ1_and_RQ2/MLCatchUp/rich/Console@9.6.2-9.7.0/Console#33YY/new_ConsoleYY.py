from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(color_system='auto', force_jupyter=None, width=80, force_terminal=None, theme=Theme(), soft_wrap=False, file=sys.stdout, height=25, stderr=False, no_color=None)
