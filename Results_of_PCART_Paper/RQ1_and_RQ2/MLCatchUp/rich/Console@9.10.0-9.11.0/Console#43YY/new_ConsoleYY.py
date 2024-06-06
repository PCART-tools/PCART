from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(file=sys.stdout, record=False, emoji=True, theme=Theme(), width=80, style='bold red', force_terminal=False, soft_wrap=False, color_system='auto', height=25, log_path=True, no_color=False, tab_size=4, markup=True, highlight=True, force_jupyter=False, log_time=True, stderr=False, force_interactive=None, quiet=False, FormatTimeCallable]='[%X]')
