import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(logging.INFO, rich_tracebacks=True, markup=False, enable_link_path=True, highlighter=ReprHighlighter(), tracebacks_width=80, show_time=True, show_level=True, show_path=True, tracebacks_show_locals=False)
