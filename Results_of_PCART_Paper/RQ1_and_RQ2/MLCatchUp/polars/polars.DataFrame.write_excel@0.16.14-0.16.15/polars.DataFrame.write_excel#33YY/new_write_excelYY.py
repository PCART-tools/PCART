import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(position='A1', row_heights=None, float_precision=3, hide_gridlines=False, dtype_formats=None, autofit=False, column_formats=None, column_widths=None, conditional_formats=None, hidden_columns=None, table_name=None, has_header=True, table_style=None, sparklines=None, column_totals=None, autofilter=True)
