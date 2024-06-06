import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(show_path=True, show_time=True, console=Console(), enable_link_path=True, level=logging.INFO, show_level=True, tracebacks_show_locals=False)
