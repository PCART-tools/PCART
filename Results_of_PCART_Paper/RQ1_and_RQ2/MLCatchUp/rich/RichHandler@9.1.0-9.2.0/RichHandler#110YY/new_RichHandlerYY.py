import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(logging.INFO, tracebacks_width=80, tracebacks_extra_lines=3, markup=False, highlighter=ReprHighlighter(), console=Console(), tracebacks_theme='monokai', rich_tracebacks=True, show_level=True, tracebacks_word_wrap=True, enable_link_path=True, show_path=True, show_time=True, tracebacks_show_locals=False)
