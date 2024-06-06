from rich.progress import track
from rich.console import Console
console = Console()
sequence = range(100)
track(sequence, 'Working...', None, True, console, False, get_time=None, refresh_per_second=10, style='bar.back', complete_style='bar.complete', show_speed=True)
