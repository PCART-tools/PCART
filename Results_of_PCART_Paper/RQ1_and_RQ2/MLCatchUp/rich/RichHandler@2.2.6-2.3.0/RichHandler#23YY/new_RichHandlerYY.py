import logging
from rich.logging import RichHandler
handler = RichHandler(level=logging.NOTSET, enable_link_path=True, console=None, highlighter=None)
