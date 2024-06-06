from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(record=False, no_color=False, width=80, file=sys.stdout, theme=Theme(), tab_size=4, emoji=True, highlight=True, color_system='auto', markup=True, height=25, force_terminal=False, style='bold red', log_time=True, soft_wrap=False, stderr=False, force_jupyter=False, force_interactive=None, quiet=False, FormatTimeCallable]='[%X]')
