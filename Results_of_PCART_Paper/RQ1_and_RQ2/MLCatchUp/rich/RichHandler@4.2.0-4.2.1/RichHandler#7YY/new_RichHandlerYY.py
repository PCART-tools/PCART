import logging
from rich.console import Console
from rich.logging import RichHandler
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(enable_link_path=True, highlighter=ReprHighlighter(), show_path=True, show_time=True, show_level=True)
