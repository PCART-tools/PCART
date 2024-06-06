import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(tracebacks_width=80, markup=False, show_level=True, tracebacks_extra_lines=3, enable_link_path=True, highlighter=ReprHighlighter(), level=logging.INFO, rich_tracebacks=True, show_path=True, show_time=True, tracebacks_theme='monokai', tracebacks_show_locals=False)
