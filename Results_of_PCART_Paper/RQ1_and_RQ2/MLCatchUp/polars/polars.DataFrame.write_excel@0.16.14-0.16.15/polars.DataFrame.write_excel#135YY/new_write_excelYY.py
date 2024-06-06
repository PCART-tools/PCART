import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(None,  None, row_heights=None, hidden_columns=None, has_header=True, table_style=None, column_formats=None, sparklines=None, hide_gridlines=False, float_precision=3, dtype_formats=None, autofilter=True, column_widths=None, autofit=False, table_name=None, position='A1', conditional_formats=None, column_totals=None)
