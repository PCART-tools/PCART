from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(markup=True, record=False, theme=Theme(), soft_wrap=False, width=80, emoji=True, color_system='auto', stderr=False, height=25, force_jupyter=None, force_terminal=None, tab_size=4, file=sys.stdout, style='bold red', highlight=True, no_color=None)
