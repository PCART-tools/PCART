import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(show_level=True, level=logging.INFO, markup=False, show_path=True, enable_link_path=True, highlighter=ReprHighlighter(), show_time=True, tracebacks_show_locals=False)
