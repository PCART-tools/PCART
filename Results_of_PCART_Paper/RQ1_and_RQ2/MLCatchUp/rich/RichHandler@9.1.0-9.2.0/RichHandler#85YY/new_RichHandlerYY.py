import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(logging.INFO, Console(), markup=False, show_level=True, show_path=True, show_time=True, tracebacks_width=80, rich_tracebacks=True, highlighter=ReprHighlighter(), enable_link_path=True, tracebacks_show_locals=False)
