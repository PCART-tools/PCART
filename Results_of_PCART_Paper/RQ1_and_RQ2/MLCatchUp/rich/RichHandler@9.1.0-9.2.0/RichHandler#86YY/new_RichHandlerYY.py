import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(logging.INFO, Console(), tracebacks_extra_lines=3, tracebacks_width=80, rich_tracebacks=True, highlighter=ReprHighlighter(), show_path=True, markup=False, show_level=True, enable_link_path=True, show_time=True, tracebacks_show_locals=False)
