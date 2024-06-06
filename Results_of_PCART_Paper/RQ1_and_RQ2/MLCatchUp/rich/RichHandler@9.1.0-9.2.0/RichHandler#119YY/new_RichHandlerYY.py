import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(console=Console(), level=logging.INFO, tracebacks_width=80, tracebacks_show_locals=False)
