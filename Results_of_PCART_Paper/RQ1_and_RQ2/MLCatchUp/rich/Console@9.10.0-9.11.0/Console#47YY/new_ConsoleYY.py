from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(stderr=False, log_time_format='[%X]', soft_wrap=False, width=80, safe_box=True, force_jupyter=False, log_time=True, highlighter=ReprHighlighter(), markup=True, legacy_windows=None, file=sys.stdout, log_path=True, tab_size=4, no_color=False, force_terminal=False, style='bold red', emoji=True, height=25, theme=Theme(), color_system='auto', record=False, highlight=True, force_interactive=None, quiet=False, FormatTimeCallable]='[%X]')
