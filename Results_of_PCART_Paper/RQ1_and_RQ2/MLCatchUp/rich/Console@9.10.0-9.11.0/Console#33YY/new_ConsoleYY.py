from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(color_system='auto', file=sys.stdout, width=80, stderr=False, force_jupyter=False, soft_wrap=False, force_terminal=False, theme=Theme(), force_interactive=None, quiet=False, FormatTimeCallable]='[%X]')
