import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(logging.INFO, Console(), markup=False, rich_tracebacks=True, show_level=True, show_time=True, show_path=True, enable_link_path=True, highlighter=ReprHighlighter(), tracebacks_show_locals=False)
