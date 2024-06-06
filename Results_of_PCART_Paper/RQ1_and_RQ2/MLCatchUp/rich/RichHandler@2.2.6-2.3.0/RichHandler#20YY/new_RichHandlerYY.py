import logging
from rich.logging import RichHandler
handler = RichHandler(logging.NOTSET, show_path=True, console=None, enable_link_path=True, highlighter=None)
