from rich.columns import Columns
from rich.text import Text
columns = Columns(equal=False, expand=False, renderables=[Text('Column 1'), Text('Column 2')], width=20, padding=(0, 1), title=None)
