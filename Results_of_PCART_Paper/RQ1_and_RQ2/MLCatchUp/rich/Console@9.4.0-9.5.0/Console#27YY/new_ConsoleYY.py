from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(file=sys.stdout, color_system='auto', force_jupyter=None, force_terminal=None, theme=Theme(), width=80, soft_wrap=False, stderr=False, style=None)
