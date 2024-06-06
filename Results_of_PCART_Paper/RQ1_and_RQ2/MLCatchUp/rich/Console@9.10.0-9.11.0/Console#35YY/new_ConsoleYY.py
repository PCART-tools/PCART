from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(force_jupyter=False, soft_wrap=False, height=25, theme=Theme(), stderr=False, style='bold red', color_system='auto', width=80, file=sys.stdout, force_terminal=False, force_interactive=None, quiet=False, FormatTimeCallable]='[%X]')
