import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(console=Console(), show_time=True, level=logging.INFO, show_path=True, show_level=True, tracebacks_show_locals=False)
