import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(logging.INFO, highlighter=ReprHighlighter(), show_level=True, markup=False, console=Console(), enable_link_path=True, rich_tracebacks=True, show_time=True, show_path=True, tracebacks_show_locals=False)
