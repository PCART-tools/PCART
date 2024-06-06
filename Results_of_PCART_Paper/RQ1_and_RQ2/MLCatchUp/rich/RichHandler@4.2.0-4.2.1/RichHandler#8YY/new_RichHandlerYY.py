import logging
from rich.console import Console
from rich.logging import RichHandler
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(show_path=True, highlighter=ReprHighlighter(), enable_link_path=True, markup=False, show_time=True, show_level=True)
