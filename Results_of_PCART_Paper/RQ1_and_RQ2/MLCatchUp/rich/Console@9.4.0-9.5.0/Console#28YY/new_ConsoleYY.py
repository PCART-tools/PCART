from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(color_system='auto', height=25, force_jupyter=None, file=sys.stdout, force_terminal=None, width=80, theme=Theme(), soft_wrap=False, stderr=False, style=None)
