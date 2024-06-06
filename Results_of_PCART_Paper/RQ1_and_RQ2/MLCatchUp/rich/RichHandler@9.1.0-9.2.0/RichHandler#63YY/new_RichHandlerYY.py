import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(highlighter=ReprHighlighter(), show_level=True, show_path=True, markup=False, tracebacks_width=80, enable_link_path=True, rich_tracebacks=True, level=logging.INFO, show_time=True, tracebacks_show_locals=False)
