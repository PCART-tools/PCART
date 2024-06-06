import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(None, column_formats=None, hidden_columns=None, conditional_formats=None, sparklines=None, table_style=None, hide_gridlines=False, sheet_zoom=None, column_totals=None, position='A1', float_precision=3, autofit=False, row_heights=None, column_widths=None, table_name=None, dtype_formats=None, autofilter=True, has_header=True)
