from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(force_terminal=None, width=80, markup=True, record=False, theme=Theme(), height=25, file=sys.stdout, emoji=True, force_jupyter=None, tab_size=4, color_system='auto', highlight=True, soft_wrap=False, stderr=False, style=None)
