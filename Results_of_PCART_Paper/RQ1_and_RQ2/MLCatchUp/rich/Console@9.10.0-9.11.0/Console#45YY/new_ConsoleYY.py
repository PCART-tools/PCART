from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(tab_size=4, markup=True, force_jupyter=False, height=25, color_system='auto', highlight=True, soft_wrap=False, highlighter=ReprHighlighter(), force_terminal=False, emoji=True, no_color=False, style='bold red', log_time=True, file=sys.stdout, theme=Theme(), log_path=True, record=False, stderr=False, log_time_format='[%X]', width=80, force_interactive=None, quiet=False, FormatTimeCallable]='[%X]')
