import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(logging.INFO, markup=False, rich_tracebacks=True, highlighter=ReprHighlighter(), console=Console(), tracebacks_width=80, show_level=True, enable_link_path=True, show_path=True, show_time=True, tracebacks_show_locals=False)
