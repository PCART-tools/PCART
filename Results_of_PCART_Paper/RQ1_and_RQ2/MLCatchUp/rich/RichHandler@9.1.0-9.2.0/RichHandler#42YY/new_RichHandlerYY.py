import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(logging.INFO, show_path=True, tracebacks_width=80, show_time=True, show_level=True, tracebacks_extra_lines=3, markup=False, rich_tracebacks=True, enable_link_path=True, highlighter=ReprHighlighter(), tracebacks_show_locals=False)
