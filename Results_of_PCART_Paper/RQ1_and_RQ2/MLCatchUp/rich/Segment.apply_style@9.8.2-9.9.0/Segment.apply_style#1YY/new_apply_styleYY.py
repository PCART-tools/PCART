from rich.segment import Segment
from rich.style import Style
segments = [Segment('Hello'), Segment('World')]
styled_segments = Segment.apply_style(segments, post_style=None)
