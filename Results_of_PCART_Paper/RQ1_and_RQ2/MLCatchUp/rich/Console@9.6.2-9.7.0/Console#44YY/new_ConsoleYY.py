from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(highlight=True, width=80, soft_wrap=False, log_time=True, file=sys.stdout, tab_size=4, log_time_format='[%X]', highlighter=ReprHighlighter(), force_jupyter=None, log_path=True, stderr=False, style='bold red', legacy_windows=None, height=25, force_terminal=None, record=False, theme=Theme(), color_system='auto', markup=True, emoji=True, no_color=None)
