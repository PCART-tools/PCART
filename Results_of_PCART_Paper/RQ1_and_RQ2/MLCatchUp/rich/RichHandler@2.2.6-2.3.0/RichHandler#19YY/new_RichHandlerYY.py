import logging
from rich.logging import RichHandler
handler = RichHandler(logging.NOTSET, console=None, enable_link_path=True, highlighter=None)
