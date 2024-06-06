from rich.progress import track
from rich.console import Console
console = Console()
sequence = range(100)
track(sequence, 'Working...', None, auto_refresh=True, console=console, show_speed=True)
