import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(logging.INFO, tracebacks_theme='monokai', show_path=True, enable_link_path=True, tracebacks_extra_lines=3, markup=False, highlighter=ReprHighlighter(), rich_tracebacks=True, show_level=True, tracebacks_word_wrap=True, tracebacks_width=80, show_time=True, tracebacks_show_locals=False)
