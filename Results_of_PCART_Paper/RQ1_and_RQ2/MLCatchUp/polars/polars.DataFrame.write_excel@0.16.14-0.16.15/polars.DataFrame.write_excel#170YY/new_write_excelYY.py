import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(None, column_widths=None, row_heights=None, sheet_zoom=None, column_totals=None, autofilter=True, table_name=None, has_header=True, worksheet=None, dtype_formats=None, autofit=False, position='A1', conditional_formats=None, float_precision=3, hidden_columns=None, column_formats=None, hide_gridlines=False, sparklines=None, table_style=None)
