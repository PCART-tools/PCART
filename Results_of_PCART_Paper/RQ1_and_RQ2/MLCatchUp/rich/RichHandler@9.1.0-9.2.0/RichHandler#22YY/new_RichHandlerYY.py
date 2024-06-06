import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(show_path=True, highlighter=ReprHighlighter(), tracebacks_extra_lines=3, tracebacks_theme='monokai', rich_tracebacks=True, tracebacks_width=80, tracebacks_word_wrap=True, enable_link_path=True, markup=False, show_time=True, show_level=True, tracebacks_show_locals=False)
