import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(show_level=True, level=logging.INFO, tracebacks_show_locals=False)
