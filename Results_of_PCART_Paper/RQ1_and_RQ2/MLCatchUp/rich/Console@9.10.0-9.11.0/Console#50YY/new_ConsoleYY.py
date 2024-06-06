from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(style='bold red', highlighter=ReprHighlighter(), soft_wrap=False, width=80, get_time=datetime.now().timestamp, safe_box=True, log_path=True, legacy_windows=None, log_time_format='[%X]', theme=Theme(), log_time=True, height=25, emoji=True, force_jupyter=False, stderr=False, file=sys.stdout, markup=True, get_datetime=datetime.now, tab_size=4, highlight=True, no_color=False, _environ={}, color_system='auto', force_terminal=False, record=False, force_interactive=None, quiet=False, FormatTimeCallable]='[%X]')
