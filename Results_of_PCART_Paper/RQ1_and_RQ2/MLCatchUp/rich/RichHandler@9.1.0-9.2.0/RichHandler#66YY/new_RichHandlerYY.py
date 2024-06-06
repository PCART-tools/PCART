import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(tracebacks_theme='monokai', level=logging.INFO, enable_link_path=True, tracebacks_width=80, tracebacks_word_wrap=True, show_path=True, show_level=True, highlighter=ReprHighlighter(), show_time=True, markup=False, rich_tracebacks=True, tracebacks_extra_lines=3, tracebacks_show_locals=False)
