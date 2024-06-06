from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(tab_size=4, width=80, theme=Theme(), force_terminal=None, file=sys.stdout, force_jupyter=None, color_system='auto', height=25, soft_wrap=False, stderr=False, style=None)
