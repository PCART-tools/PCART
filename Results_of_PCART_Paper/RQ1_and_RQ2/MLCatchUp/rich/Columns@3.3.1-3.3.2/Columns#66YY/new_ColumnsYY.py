from rich.columns import Columns
from rich.text import Text
columns = Columns(renderables=[Text('Column 1'), Text('Column 2')], right_to_left=False, padding=(0, 1), title=None)
