import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(level=logging.INFO, show_path=True, highlighter=ReprHighlighter(), enable_link_path=True, console=Console(), show_level=True, show_time=True, tracebacks_show_locals=False)
