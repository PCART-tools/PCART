from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(style='bold red', no_color=False, emoji=True, log_path=True, force_jupyter=False, force_terminal=False, file=sys.stdout, get_datetime=datetime.now, width=80, tab_size=4, log_time_format='[%X]', stderr=False, soft_wrap=False, highlight=True, markup=True, record=False, legacy_windows=None, log_time=True, height=25, color_system='auto', theme=Theme(), safe_box=True, highlighter=ReprHighlighter(), force_interactive=None, quiet=False, FormatTimeCallable]='[%X]')
