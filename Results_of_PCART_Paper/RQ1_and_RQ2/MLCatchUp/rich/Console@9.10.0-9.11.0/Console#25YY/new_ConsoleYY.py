from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(get_time=datetime.now().timestamp, force_interactive=None, quiet=False, FormatTimeCallable]='[%X]')
