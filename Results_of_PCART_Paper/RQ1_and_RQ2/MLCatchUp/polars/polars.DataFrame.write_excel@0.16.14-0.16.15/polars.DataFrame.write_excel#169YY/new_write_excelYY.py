import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(None, hide_gridlines=False, row_heights=None, column_formats=None, dtype_formats=None, has_header=True, autofit=False, float_precision=3, position='A1', column_totals=None, worksheet=None, conditional_formats=None, table_style=None, autofilter=True, table_name=None, sparklines=None, hidden_columns=None, column_widths=None)
