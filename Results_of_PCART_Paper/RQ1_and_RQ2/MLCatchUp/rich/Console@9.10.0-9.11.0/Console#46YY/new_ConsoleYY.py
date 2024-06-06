from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(emoji=True, file=sys.stdout, log_path=True, highlighter=ReprHighlighter(), highlight=True, log_time_format='[%X]', theme=Theme(), soft_wrap=False, tab_size=4, stderr=False, style='bold red', force_jupyter=False, record=False, markup=True, height=25, legacy_windows=None, force_terminal=False, log_time=True, color_system='auto', no_color=False, width=80, force_interactive=None, quiet=False, FormatTimeCallable]='[%X]')
