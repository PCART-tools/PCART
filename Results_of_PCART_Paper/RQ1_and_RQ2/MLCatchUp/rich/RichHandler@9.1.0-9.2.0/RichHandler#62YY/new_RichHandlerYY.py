import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(show_level=True, rich_tracebacks=True, show_time=True, show_path=True, highlighter=ReprHighlighter(), markup=False, level=logging.INFO, enable_link_path=True, tracebacks_show_locals=False)
