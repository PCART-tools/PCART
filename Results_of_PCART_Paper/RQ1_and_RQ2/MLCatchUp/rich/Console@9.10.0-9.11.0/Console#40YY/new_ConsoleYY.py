from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(stderr=False, width=80, theme=Theme(), no_color=False, style='bold red', force_jupyter=False, markup=True, height=25, color_system='auto', emoji=True, record=False, force_terminal=False, file=sys.stdout, soft_wrap=False, tab_size=4, force_interactive=None, quiet=False, FormatTimeCallable]='[%X]')
