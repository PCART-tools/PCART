import logging
from rich.logging import RichHandler
handler = RichHandler(console=None, show_path=True, enable_link_path=True, level=logging.NOTSET, highlighter=None)
