from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(soft_wrap=False, force_terminal=False, height=25, force_jupyter=False, markup=True, record=False, no_color=False, width=80, color_system='auto', emoji=True, style='bold red', file=sys.stdout, tab_size=4, theme=Theme(), highlight=True, stderr=False, force_interactive=None, quiet=False, FormatTimeCallable]='[%X]')
