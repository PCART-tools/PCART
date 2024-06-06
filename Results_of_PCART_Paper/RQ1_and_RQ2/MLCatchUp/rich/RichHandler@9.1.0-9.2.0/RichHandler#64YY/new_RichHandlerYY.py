import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(tracebacks_width=80, tracebacks_extra_lines=3, markup=False, enable_link_path=True, show_level=True, show_time=True, level=logging.INFO, highlighter=ReprHighlighter(), show_path=True, rich_tracebacks=True, tracebacks_show_locals=False)
