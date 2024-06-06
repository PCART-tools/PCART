from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(width=80, highlight=True, log_time=True, log_path=True, theme=Theme(), markup=True, tab_size=4, log_time_format='[%X]', emoji=True, no_color=False, file=sys.stdout, record=False, soft_wrap=False, height=25, style='bold red', color_system='auto', force_terminal=False, force_jupyter=False, stderr=False, force_interactive=None, quiet=False, FormatTimeCallable]='[%X]')
