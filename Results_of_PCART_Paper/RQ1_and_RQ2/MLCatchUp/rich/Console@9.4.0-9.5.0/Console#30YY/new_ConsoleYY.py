from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(height=25, force_terminal=None, width=80, force_jupyter=None, color_system='auto', record=False, theme=Theme(), file=sys.stdout, tab_size=4, soft_wrap=False, stderr=False, style=None)
