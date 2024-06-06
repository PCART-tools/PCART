from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(stderr=False, color_system='auto', theme=Theme(), width=80, file=sys.stdout, style='bold red', force_terminal=None, tab_size=4, force_jupyter=None, soft_wrap=False, height=25, no_color=None)
