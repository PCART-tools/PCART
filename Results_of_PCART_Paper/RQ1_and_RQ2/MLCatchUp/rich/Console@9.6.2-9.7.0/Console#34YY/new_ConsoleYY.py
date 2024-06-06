from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(force_jupyter=None, theme=Theme(), file=sys.stdout, width=80, soft_wrap=False, height=25, color_system='auto', force_terminal=None, style='bold red', stderr=False, no_color=None)
