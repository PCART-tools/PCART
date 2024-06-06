from rich.progress import track
from rich.console import Console
console = Console()
sequence = range(100)
track(sequence, 'Working...', None, True, console, False, None, 10, style='bar.back', complete_style='bar.complete', finished_style='bar.finished', show_speed=True)
