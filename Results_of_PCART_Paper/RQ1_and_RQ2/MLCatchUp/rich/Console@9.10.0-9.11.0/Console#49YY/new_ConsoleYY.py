from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(soft_wrap=False, tab_size=4, highlight=True, log_time_format='[%X]', get_time=datetime.now().timestamp, markup=True, force_jupyter=False, record=False, no_color=False, theme=Theme(), width=80, safe_box=True, log_path=True, get_datetime=datetime.now, stderr=False, height=25, legacy_windows=None, file=sys.stdout, style='bold red', highlighter=ReprHighlighter(), color_system='auto', log_time=True, force_terminal=False, emoji=True, force_interactive=None, quiet=False, FormatTimeCallable]='[%X]')
