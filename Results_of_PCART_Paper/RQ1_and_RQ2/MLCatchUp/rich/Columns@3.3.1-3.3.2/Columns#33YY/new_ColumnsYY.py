from rich.columns import Columns
from rich.text import Text
columns = Columns(width=20, equal=False, expand=False, renderables=[Text('Column 1'), Text('Column 2')], title=None)
