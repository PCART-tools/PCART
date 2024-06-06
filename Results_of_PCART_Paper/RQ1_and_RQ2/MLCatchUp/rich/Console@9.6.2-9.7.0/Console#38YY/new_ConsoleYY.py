from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(force_terminal=None, tab_size=4, style='bold red', height=25, stderr=False, markup=True, record=False, file=sys.stdout, emoji=True, width=80, theme=Theme(), color_system='auto', force_jupyter=None, soft_wrap=False, no_color=None)
