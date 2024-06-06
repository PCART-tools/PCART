import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(rich_tracebacks=True, show_time=True, markup=False, show_level=True, highlighter=ReprHighlighter(), tracebacks_width=80, show_path=True, enable_link_path=True, tracebacks_extra_lines=3, tracebacks_show_locals=False)
