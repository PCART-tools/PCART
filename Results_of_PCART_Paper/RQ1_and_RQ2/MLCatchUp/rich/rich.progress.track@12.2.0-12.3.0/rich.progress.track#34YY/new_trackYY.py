from rich.progress import track
from rich.console import Console
console = Console()
sequence = range(100)
track(sequence, description='Working...', total=None, auto_refresh=True, console=console, transient=False, get_time=None, show_speed=True)
