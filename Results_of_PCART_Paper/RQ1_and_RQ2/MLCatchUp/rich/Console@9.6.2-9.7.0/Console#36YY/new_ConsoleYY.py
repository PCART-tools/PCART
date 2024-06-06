from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(soft_wrap=False, color_system='auto', record=False, stderr=False, height=25, file=sys.stdout, tab_size=4, width=80, style='bold red', force_jupyter=None, theme=Theme(), force_terminal=None, no_color=None)
