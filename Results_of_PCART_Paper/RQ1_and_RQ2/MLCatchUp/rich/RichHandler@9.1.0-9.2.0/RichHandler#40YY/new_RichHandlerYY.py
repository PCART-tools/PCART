import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(logging.INFO, show_level=True, markup=False, show_time=True, show_path=True, rich_tracebacks=True, highlighter=ReprHighlighter(), enable_link_path=True, tracebacks_show_locals=False)
